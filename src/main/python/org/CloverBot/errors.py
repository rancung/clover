from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, bot):
        self.author = None
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(error)
        if isinstance(error, commands.MissingRequiredArgument):
            await self.ctx.send('No command found')
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send(error)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(error)
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(error)
        if isinstance(error, commands.RoleNotFound):
            await ctx.send(error)

def setup(bot):
    bot.add_cog(Errors(bot))