import random
import aiohttp
import datetime
from discord.ext import tasks, commands
import discord
import loadconfig


class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    @commands.command(help='Change bot status ex. :changestatus dnd')
    @commands.has_role('moderator')
    async def changestatus(self, ctx, status: str):
        status = status.lower()
        if status == 'offline' or status == 'off' or status == 'invisible':
            discord_status = discord.Status.invisible
        elif status == 'idle':
            discord_status = discord.Status.idle
        elif status == 'dnd' or status == 'disturb':
            discord_status = discord.Status.dnd
        else:
            discord_status = discord.Status.online
        await self.bot.change_presence(status=discord_status)
        await ctx.send(f'**:ok:** Status set: **{discord_status}**')

    @commands.command(help='Say things as bot in a chat ex. :echo #general-chit-chat hi yo')
    @commands.has_role('moderator')
    async def echo(self, ctx, channel: discord.TextChannel, *message: str):
        if not channel.permissions_for(ctx.message.author).read_messages == True:
            return await ctx.send("You're not allowed to access that channel.")
        try:
            msg = ' '.join(message)
            return await channel.send(msg)
        except discord.errors.Forbidden:
            return await ctx.send("No permissions to read that channel.")

    @commands.command(help='Generate an invite for a channel ex. :geninvite #general-chit-chat')
    @commands.has_role('moderator')
    async def geninvite(self, ctx, channel: discord.TextChannel):
        invite = await channel.create_invite(max_age=300, max_uses=1, unique=True)
        msg = f'Invite to guild on channel {channel.name} \n{invite.url}'
        await ctx.author.send(msg)

    @commands.command(hidden=True)
    @commands.has_role('moderator')
    async def hierarchy(self, ctx):
        msg = f'Roll Hierarchy **{ctx.guild}**:\n\n'
        role_dict = {}

        for role in ctx.guild.roles:
            if role.is_default():
                role_dict[role.position] = 'everyone'
            else:
                role_dict[role.position] = role.name

        for role in sorted(role_dict.items(), reverse=True):
            msg += role[1] + '\n'
        await ctx.send(msg)

    @commands.command(hidden=True)
    async def permissions(self, ctx, username:str=None):
        if username is None:
            member = ctx.me
        else:
            member = discord.utils.get(ctx.channel.guild.members, name=username)
        if member is None:
            await ctx.send("Not sure what user to check permissions for")
            return

        permissions = ctx.channel.permissions_for(member)
        embed = discord.Embed(title=':customs:  Permissions {}'.format(member), color=0x3498db)  # Blue
        embed.add_field(name='Server', value=ctx.guild)
        embed.add_field(name='Channel', value=ctx.channel, inline=False)

        for item, valueBool in permissions:
            if valueBool == True:
                value = ':white_check_mark:'
            else:
                value = ':x:'
            embed.add_field(name=item, value=value)

        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(alies=['setrole', 'sr'])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def setrank(self, ctx, username:str, *rankName: str):
        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        member = discord.utils.get(ctx.channel.guild.members, name=username)
        if member is not None:
            await member.add_roles(rank)
            await ctx.send(f':white_check_mark: Role **{rank.name}** added to **{member.name}**')
        else:
            await ctx.send(':no_entry: Nope')


def setup(bot):
    bot.add_cog(admin(bot))
