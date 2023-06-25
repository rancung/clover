from discord.ext import commands


class Mods(commands.Cog):
    def __init__(self, bot):
        self.author = None
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')


def setup(bot):
    bot.add_cog(Mods(bot))