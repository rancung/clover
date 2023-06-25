from discord.ext import commands


class Message(commands.Cog):
    def __init__(self, bot):
        self.author = None
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        if "fuck" in message.content:
            await message.delete()
            await message.channel.send("badword")

def setup(bot):
    bot.add_cog(Message(bot))