import aiohttp
from discord.ext import tasks, commands
import discord


class DadJokes(commands.Cog):
    """Random dad jokes from icanhazdadjoke.com"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="The random dad joke you were always looking for.")
    async def dadjoke(self, ctx):
        """Gets a random dad joke."""
        api = 'https://icanhazdadjoke.com/'
        async with aiohttp.request('GET', api, headers={'Accept': 'text/plain'}) as r:
            if r.status == 200:
                result = await r.text()
                await ctx.send(f"`{result}`")
            else:
                await ctx.send("Rut roh. Something happened.")


def setup(bot):
    bot.add_cog(DadJokes(bot))
