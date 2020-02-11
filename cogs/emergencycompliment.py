import aiohttp
from discord.ext import tasks, commands
import discord
import json
from random import choice


class EmergencyCompliment(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Random compliment")
    async def compliment(self, ctx, user: discord.User = None):
        """Gets a random compliment"""

        msg = " "
        if user and user == self.bot.user:
            bot_msg = [
                "https://i.giphy.com/IcGkqdUmYLFGE.gif",
                "https://i.giphy.com/oFeUVZfiuim9G.gif"]
            return await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}")
        url = 'https://spreadsheets.google.com/feeds/list/1eEa2ra2yHBXVZ_ctH4J15tFSGEu-VTSunsrvaCAV598/od6/public/values?alt=json'
        async with aiohttp.request('GET', url, headers={'Accept': 'application/json'}) as r:
            if r.status == 200:
                result = await r.text()
                json_data = json.loads(result)
                compliments_list = json_data['feed']['entry']
                c_data = choice(compliments_list)
                compliment = c_data['gsx$compliments']['$t']
                if user:
                    return await ctx.send(user.mention + msg + compliment)
                else:
                    return await ctx.send(ctx.message.author.mention + msg + compliment)
            else:
                return await ctx.send("Rut roh. Something happened.")


def setup(bot):
    bot.add_cog(EmergencyCompliment(bot))
