import os

import discord
import discord.ext.commands as commands
import re
from datetime import datetime
import traceback
import logging
from logging.handlers import RotatingFileHandler
import loadconfig
from random import choice

logger = logging.getLogger('discord')
logger.setLevel(logging.WARN)
handler = RotatingFileHandler(filename='smartbot.log', maxBytes=1024*5, backupCount=2, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix=loadconfig.__prefix__)

from cogs import remind, fun, admin, dadjoke, chatchart, insult, emergencycompliment, conversationgames, nsfw, imgflip
remind.setup(bot)
fun.setup(bot)
admin.setup(bot)
dadjoke.setup(bot)
chatchart.setup(bot)
insult.setup(bot)
emergencycompliment.setup(bot)
conversationgames.setup(bot)
nsfw.setup(bot)
imgflip.setup(bot)


@bot.event
async def on_ready():
    print("Discord bot logged in as: %s, %s" % (bot.user.name, bot.user.id))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if re.search(r"\bmoney\b", message.content.lower()):
        money_list = ["https://i.giphy.com/mvD5KI8k6TfUc.gif",
                      "https://66.media.tumblr.com/tumblr_lcnvp9ZRgN1qckapz.gif",
                      "https://i.imgur.com/2uv87RS.jpg",
                      "Do you have a structured settlement? It's your money, use it when you need it. Call 877-CASHNOW"
                      ]
        await message.channel.send(choice(money_list))

    if re.search(r"\bbot\b", message.content.lower()):
        await message.add_reaction('👀')  # :eyes:

    if re.search(r"\b(cz|club zero|clubzero|c0)\b", message.content.lower()):
        await message.add_reaction('💩')  # :poop:

    if re.search(r"\b(slytherin)\b", message.content.lower()):
        await message.add_reaction('💩')  # :poop:

    if re.search(r"\busa\b", message.content.lower()):
        await message.add_reaction("\U0001f1fa\U0001f1f8")

    if re.search(r"\bcannibalism\b", message.content.lower()):
        await message.channel.send("That's when the cannibalism started...")

    if re.search(r"\bstroopwaffles*\b", message.content.lower()):
        await message.channel.send("We need to remember what's important in life: friends, waffles, "
                                   "work. Or waffles, friends, work. Doesn't matter, but work is third.")

    if re.search(r"\b(chuckle|snort)\b", message.content.lower()):
        await message.add_reaction('💩')
        await message.channel.send(f'Bad {message.author}')

    if re.search(r"\bplatypus\b", message.content.lower()):
        await message.add_reaction("\U0001fa93")

    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'help' in message.content.lower():
            await message.channel.send(
                'Type "{}help" for a list of commands'.format(bot.command_prefix))
        else:
            await message.add_reaction('👀')  # :eyes:

    await bot.process_commands(message)


@bot.event
async def on_error(event, *args, **kwargs):
    embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red
    embed.add_field(name='Event', value=event)
    embed.description = '```py\n%s\n```' % traceback.format_exc()
    embed.timestamp = datetime.utcnow()
    try:
        await bot.get_user(667822356328349706).send(embed=embed)
    except:
        pass


@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.author.send('This command cannot be used in private messages.')
    elif isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(title=':x: Command Error', colour=0x992d22) #Dark Red
        embed.add_field(name='Error', value=error)
        embed.add_field(name='Guild', value=ctx.guild)
        embed.add_field(name='Channel', value=ctx.channel)
        embed.add_field(name='User', value=ctx.author)
        embed.add_field(name='Message', value=ctx.message.clean_content)
        embed.timestamp = datetime.utcnow()
        try:
            await bot.get_user(667822356328349706).send(embed=embed)
        except:
            pass


if __name__ == "__main__":
    bot.run(loadconfig.__token__)
