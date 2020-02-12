import discord

from discord.ext import commands

from typing import Union

from . import constants as sub
from .core import Core, nsfwcheck


class Nsfw(Core):
    """
    Send random NSFW images from random subreddits

    If `[p]help Nsfw` or any other Nsfw commands are used in a non-nsfw channel,
    you will not be able to see the list of commands for this category.
    """

    @nsfwcheck()
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cleandm(self, ctx: commands.Context, number: int):
        """
            Delete a number specified of DM's from the bot.

            `<number>`: Number of messages from the bot you want
            to delete in your DM's.
        """
        if ctx.guild:
            return await ctx.send("This command works only for DM's messages !")
        async for message in ctx.channel.history(limit=number):
            if message.author.id == ctx.bot.user.id:
                await message.delete()
        await ctx.tick()

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(name="4k", aliases=["4K", "fourk"])
    async def four_k(self, ctx: commands.Context):
        """Show some 4k images from random subreddits."""

        await self._send_msg(ctx, "4k", sub=sub.FOUR_K)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["oface", "ofaces"])
    async def ahegao(self, ctx: commands.Context):
        """Show some ahegao images from random subreddits."""

        await self._send_msg(ctx, "ahegao", sub=sub.AHEGAO)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["butt", "booty"])
    async def ass(self, ctx: commands.Context):
        """Show some ass images from random subreddits."""

        await self._send_msg(ctx, "ass", sub=sub.ASS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["sodomy"])
    async def anal(self, ctx: commands.Context):
        """Show some anal images/gifs from random subreddits."""

        await self._send_msg(ctx, "anal", sub=sub.ANAL)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["shibari"])
    async def bdsm(self, ctx: commands.Context):
        """Show some bdsm from random subreddits."""

        await self._send_msg(ctx, "bdsm", sub=sub.BDSM)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["blackdick", "bcock", "bdick", "blackcocks", "blackdicks"])
    async def blackcock(self, ctx: commands.Context):
        """Show some blackcock images from random subreddits."""

        await self._send_msg(ctx, "black cock", sub=sub.BLACKCOCK)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["blowjobs", "blowj", "bjob", "fellatio", "fellation"])
    async def blowjob(self, ctx: commands.Context):
        """Show some blowjob images/gifs from random subreddits."""

        await self._send_msg(ctx, "blowjob", sub=sub.BLOWJOB)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["boob", "boobies", "tits", "titties", "breasts", "breast"])
    async def boobs(self, ctx: commands.Context):
        """Show some boobs images from random subreddits."""

        await self._send_msg(ctx, "boobs", sub=sub.BOOBS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["boless", "b_less"])
    async def bottomless(self, ctx: commands.Context):
        """Show some bottomless images from random subreddits."""

        await self._send_msg(ctx, "bottomless", sub=sub.BOTTOMLESS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command()
    async def cosplay(self, ctx: commands.Context):
        """Show some nsfw cosplay images from random subreddits."""

        await self._send_msg(ctx, "nsfw cosplay", sub=sub.COSPLAY)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["cunni", "pussyeating"])
    async def cunnilingus(self, ctx: commands.Context):
        """Show some cunnilingus images from random subreddits."""

        await self._send_msg(ctx, "cunnilingus", sub=sub.CUNNI)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["cum", "cums", "cumshots"])
    async def cumshot(self, ctx: commands.Context):
        """Show some cumshot images/gifs from random subreddits."""

        await self._send_msg(ctx, "cumshot", sub=sub.CUMSHOTS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["deept", "deepthroating"])
    async def deepthroat(self, ctx: commands.Context):
        """Show some deepthroat images from random subreddits."""

        await self._send_msg(ctx, "deepthroat", sub=sub.DEEPTHROAT)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["cock"])
    async def dick(self, ctx: commands.Context):
        """Show some dicks images from random subreddits."""

        await self._send_msg(ctx, "dick", sub=sub.DICK)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["doublep", "dpenetration", "doublepene", "doublepen"])
    async def doublepenetration(self, ctx: commands.Context):
        """Show some double penetration images/gifs from random subreddits."""

        await self._send_msg(ctx, "double penetration", sub=sub.DOUBLE_P)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["facial"])
    async def facials(self, ctx: commands.Context):
        """Show some facials images from random subreddits."""

        await self._send_msg(ctx, "facials", sub=sub.FACIALS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["feets", "feetish"])
    async def feet(self, ctx: commands.Context):
        """Show some feet images from random subreddits."""

        await self._send_msg(ctx, "feets", sub=sub.FEET)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command()
    async def femdom(self, ctx: commands.Context):
        """Show some femdom images from random subreddits."""

        await self._send_msg(ctx, "femdom", sub=sub.FEMDOM)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["futanari"])
    async def futa(self, ctx: commands.Context):
        """Show some futa images from random subreddits."""

        await self._send_msg(ctx, "futa", sub=sub.FUTA)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["gpp"])
    async def gay(self, ctx: commands.Context):
        """Show some gay porn from random subreddits."""

        await self._send_msg(ctx, "gay porn", sub=sub.GAY_P)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["groups", "nudegroup", "nudegroups"])
    async def group(self, ctx: commands.Context):
        """Show some groups nudes from random subreddits."""

        await self._send_msg(ctx, "groups nudes", sub=sub.GROUPS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["hentaigif"])
    async def hentai(self, ctx: commands.Context):
        """Show some hentai images/gifs from Nekobot API."""

        await self._send_other_msg(
            ctx,
            name="hentai",
            arg="message",
            source="Nekobot API",
            url=sub.NEKOBOT_URL.format(sub.NEKOBOT_HENTAI),
        )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["lesbians"])
    async def lesbian(self, ctx: commands.Context):
        """Show some lesbian gifs or images from random subreddits."""

        await self._send_msg(ctx, "lesbian", sub=sub.LESBIANS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["milfs"])
    async def milf(self, ctx: commands.Context):
        """Show some milf images from random subreddits."""

        await self._send_msg(ctx, "milf", sub=sub.MILF)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["nekogifs"])
    async def nekogif(self, ctx: commands.Context):
        """Show some neko gifs from Nekobot API."""

        await self._send_other_msg(
            ctx,
            name="neko gif",
            arg="message",
            source="Nekobot API",
            url=sub.NEKOBOT_URL.format("hneko"),
        )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["oralsex"])
    async def oral(self, ctx: commands.Context):
        """Show some oral gifs or images from random subreddits."""

        await self._send_msg(ctx, "oral", sub=sub.ORAL)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["pgif", "prongif"])
    async def porngif(self, ctx: commands.Context):
        """Show some porn gifs from Nekobot API."""

        await self._send_other_msg(
            ctx,
            name="porn gif",
            arg="message",
            source="Nekobot API",
            url=sub.NEKOBOT_URL.format("pgif"),
        )

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["flashinggirl"])
    async def public(self, ctx: commands.Context):
        """Show some public nude images from random subreddits."""

        await self._send_msg(ctx, "public nude", sub=sub.PUBLIC)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["vagina", "puss"])
    async def pussy(self, ctx: commands.Context):
        """Show some pussy nude images from random subreddits."""

        await self._send_msg(ctx, "pussy", sub=sub.PUSSY)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command()
    async def realgirls(self, ctx: commands.Context):
        """Show some real girls images from random subreddits."""

        await self._send_msg(ctx, "real nudes", sub=sub.REAL_GIRLS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["redheads", "ginger", "gingers"])
    async def redhead(self, ctx: commands.Context):
        """Show some red heads images from random subreddits."""

        await self._send_msg(ctx, "red head", sub=sub.REDHEADS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["r34"])
    async def rule34(self, ctx: commands.Context):
        """Show some rule34 images from random subreddits."""

        await self._send_msg(ctx, "rule34", sub=sub.RULE_34)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["squirts"])
    async def squirt(self, ctx: commands.Context):
        """Show some squirts images from random subreddits."""

        await self._send_msg(ctx, "squirt", sub=sub.SQUIRTS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["thighs", "legs"])
    async def thigh(self, ctx: commands.Context):
        """Show some thighs images from random subreddits."""

        await self._send_msg(ctx, "thigh", sub=sub.THIGHS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["traps", "trans", "girldick", "girldicks", "shemale", "shemales"])
    async def trap(self, ctx: commands.Context):
        """Show some traps from random subreddits."""

        await self._send_msg(ctx, "trap", sub=sub.TRAPS)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["wild", "gwild"])
    async def gonewild(self, ctx: commands.Context):
        """Show some gonewild images from random subreddits."""

        await self._send_msg(ctx, "gonewild", sub=sub.WILD)

    @nsfwcheck()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 0.5, commands.BucketType.user)
    @commands.command(aliases=["yiffs"])
    async def yiff(self, ctx: commands.Context):
        """Show some yiff images from random subreddits."""

        await self._send_msg(ctx, "yiff", sub=sub.YIFF)