import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No Reason!"):
        await ctx.send(f'Nice try {ctx.author.mention}!')

        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot kick yourself!")
            return
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member}!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Specify the amount in positive integers please.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself!")
            # print(author.role.id)
            return

        await member.ban(reason=reason)
        await ctx.send(f'Banned {member}!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    async def ping(self, ctx):
        """ Checks the ping. """
        await ctx.send(f"Pong! **{round(self.bot.latency * 1000)}ms**.")


def setup(bot):
    bot.add_cog(Admin(bot))
