import random
import urllib.parse
import sqlite3
import asyncio
import aiohttp
import discord
import re
import parsedatetime.parsedatetime as pdt
from datetime import datetime
import pytz
from pytz import timezone
import time
from discord.ext import tasks, commands


class remind(commands.Cog):
    db = 'remind.db'

    def __init__(self, bot):
        self.bot = bot
        self.setup_db()
        self.send_messages.start()

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    def cog_unload(self):
        self.send_messages.cancel()

    @tasks.loop(seconds=60.0)
    async def send_messages(self):
        await self.bot.wait_until_ready()
        print("hi, still here")

        conn, c = self.db_connect()
        current_time = datetime.now(pytz.timezone('America/New_York')).strftime('%Y-%m-%d %H:%M:%S')
        cmd = "SELECT * FROM reminders WHERE reply_date < ? AND is_sent != 1"
        c.execute(cmd, [current_time, ])

        need_to_remind_reminders = c.fetchall()
        for r in need_to_remind_reminders:
            print(r)
            user = self.bot.get_user(int(r[5]))
            if user is not None:
                print(user)
                await user.send("Hey {}. You asked me to remind you: {}".format(user.name, r[1]))
                c.execute("UPDATE reminders SET is_sent = 1 WHERE id = ?", [r[0], ])
                conn.commit()

            conn.close()

    def db_connect(self):
        db_name = self.db
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        return conn, c

    @commands.group(name='remind', help='Ex. Set reminders and I will...remind you of them')
    async def remind(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid remind command passed...')

    @remind.command(name='list', help='Ex. !remind list')
    async def remindlist(self, ctx):
        conn, c = self.db_connect()
        c.execute('SELECT * FROM reminders WHERE userid=? AND is_sent != 1 ORDER BY id asc', (ctx.message.author.id,))
        reminders = c.fetchall()
        if len(reminders) == 0:
            await ctx.send("You have no reminders")
            return
        i = 1
        for reminder in reminders:
            print(reminder)
            await ctx.send("{}) {} - Message: {}".format(i, reminder[3], reminder[1]))
            i = i + 1
        conn.close()

    @remind.command(name='delete', help='Ex. !remind delete 1')
    async def reminddelete(self, ctx, number):
        try:
            int_number = int(number)
        except ValueError:
            print(number)
            await ctx.send("Invalid number. You must pass a number")
            return
        conn, c = self.db_connect()
        c.execute('SELECT * FROM reminders WHERE userid=? AND is_sent != 1 ORDER BY id asc', (ctx.message.author.id,))
        reminders = c.fetchall()
        num_reminders = len(reminders)
        if int_number > num_reminders:
            await ctx.send("You only have {} reminders. Make sure you sent the correct number".format(num_reminders))
            return

        i = 1
        for reminder in reminders:
            print(i)
            if int_number != i:
                i = i + 1
                continue
            if int_number == i:
                c.execute("DELETE FROM reminders WHERE id = ?", (reminder[0],))
                conn.commit()
                await ctx.send("Deleted {} - Message: {}".format(reminder[3], reminder[1]))
                return
        conn.close()

    @remind.command(name='me', help='Ex. !remind me in 2 hours "message"')
    async def remindme(self, ctx):
        tmp_str = ctx.message.content
        print("user: {}, message: {}".format(ctx.message.author.name, tmp_str))
        # remove all format breaking characters IE: [ ] ( ) newline
        tmp_str = tmp_str.split("\n")[0]
        # adds " at the end if only 1 exists
        tmp_str = tmp_str.replace("“", "\"").replace("”", "\"")
        if tmp_str.count('"') <= 1:
            await ctx.send("Sorry {}. I couldn't figure out what you wanted me to do.".format(ctx.message.author.name))
            return

        # Use message default if not found
        msg_input_tmp = re.search('(["].{0,9000}["])', tmp_str)
        if msg_input_tmp:
            msg_input = msg_input_tmp.group()
            print(msg_input)
        # Fix issue with dashes for parsedatetime lib
        tmp_str = tmp_str.replace('-', "/")
        # Remove RemindMe!
        store_time = re.sub('(["].{0,9000}["])', '', tmp_str)[9:]

        cal = pdt.Calendar()
        try:

            hold_time = cal.parse(store_time, datetime.now(pytz.timezone('America/New_York')))
        except (ValueError, OverflowError):
            # year too long
            hold_time = cal.parse("9999-12-31")
        if hold_time[1] == 0:
            # default time
            hold_time = cal.parse("1 day", datetime.now(pytz.timezone('America/New_York')))
            replyMessage = "**Defaulted to one day.**\n\n"
        # Converting time
        # 9999/12/31 HH/MM/SS
        reply_date = time.strftime('%Y-%m-%d %H:%M:%S', hold_time[0])
        reply_date_time = datetime(*hold_time[0][:6], tzinfo=timezone('America/New_York'))
        save_date_time = datetime.now(pytz.timezone('America/New_York'))
        save_date = datetime.now(pytz.timezone('America/New_York')).strftime('%Y-%m-%d %H:%M:%S')
        if reply_date_time < save_date_time:
            await ctx.send("Nice try you scallywag. That date is in the past. This isn't Back to the Future")
            return

        conn, c = self.db_connect()
        c.execute(
            "INSERT INTO reminders (message, save_date, reply_date, username, userid, is_sent) VALUES(?, ?, ?, ?, ?, ?)",
            (msg_input, save_date, reply_date, ctx.message.author.name, ctx.message.author.id, 0))
        conn.commit()
        conn.close()

        await ctx.send(
            "Ok {}. I'll remind you at {} EST. Message: {}".format(ctx.message.author, reply_date, msg_input))

    def setup_db(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        # get the count of tables with the name
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='reminders' ''')

        # if the count is 1, then table exists
        if c.fetchone()[0] == 1:
            print('Reminder table exists. Not creating.')
        else:
            print("Remind table does not exist. Creating")
            # Create table
            c.execute('''CREATE TABLE reminders
                             (id INTEGER PRIMARY KEY,
                              message varchar(500) NOT NULL,
                              save_date varchar(100) NOT NULL,
                              reply_date varchar(100) NOT NULL,
                              username varchar(50) NOT NULL,
                              userid varchar(50) NOT NULL,
                              is_sent INTEGER NOT NULL
                              )
                ''')

        # commit the changes to db
        conn.commit()
        conn.close()


def setup(bot):
    bot.add_cog(remind(bot))
