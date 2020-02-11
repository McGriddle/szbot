import random
import aiohttp
import discord
from discord.ext import tasks, commands


class fun(commands.Cog):
    db = 'fun.db'

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    @commands.command(help="Show the comic of the day. Can also call :xkcd random")
    async def xkcd(self, ctx, *searchterm: str):
        apiUrl = 'https://xkcd.com{}info.0.json'
        async with aiohttp.ClientSession() as cs:
            async with cs.get(apiUrl.format('/')) as r:
                js = await r.json()
                if ''.join(searchterm) == 'random':
                    randomComic = random.randint(0, js['num'])
                    async with cs.get(apiUrl.format('/' + str(randomComic) + '/')) as r:
                        if r.status == 200:
                            js = await r.json()
                comicUrl = 'https://xkcd.com/{}/'.format(js['num'])
                date = '{}.{}.{}'.format(js['day'], js['month'], js['year'])
                msg = '**{}**\n{}\nAlt Text:```{}```XKCD Link: <{}> ({})'.format(js['safe_title'], js['img'], js['alt'],
                                                                                 comicUrl, date)
                await ctx.send(msg)

    @commands.command(name="fortune", help="Ask the magic 8 ball")
    async def eightball(self, ctx, *question: str):
        if not question:
            return await ctx.send('You gotta ask a question yo.')
        answers = ['It is certain.',
                   'It is decidedly so.',
                   'Without a doubt.',
                   'As I see it, yes.',
                   'Most likely.',
                   'Outlook good.',
                   'Reply hazy, try again.',
                   'Ask again later.',
                   'Better not tell you now.',
                   'Don\'t count on it.',
                   'My reply is no.',
                   'My sources say no.',
                   'Outlook not so good.',
                   'Very doubtful.',
                   'Yes - definitely.',
                   'Yes.',
                   'Cannot predict now.',
                   'You may rely on it.',
                   'Signs point to yes.',
                   'Concentrate and ask again.']
        embed = discord.Embed(title=':8ball:', color=0x3498db)  # Blue
        embed.add_field(name='Question', value=' '.join(str(i) for i in question))
        embed.add_field(name='Answer', value=random.choice(answers), inline=False)
        await ctx.send(embed=embed)

    @commands.command(help="Boo not cool reaction")
    async def boo(self, ctx):
        await ctx.send("https://thumbs.gfycat.com/GiddyEveryEmperorpenguin-size_restricted.gif")

    @commands.command(help="fuck you")
    async def fu(self, ctx):
        await ctx.send("https://tenor.com/view/rick-and-morty-peace-gif-10532165")


def setup(bot):
    bot.add_cog(fun(bot))
