import discord
from discord.ext import commands
from datetime import datetime

class Public(commands.Cog):
    def __init__(self, bot):
        self.author = None
        self.bot = bot
        self.time = time = datetime.now().strftime("%m/%d/%Y")

    @commands.command(
		name="userinfo",
		aliases=["whois","user"],
		brief="Find out information about other members",
		description="Find out information about other members"
	)
    async def _userinfo(self, ctx,*, member: discord.Member=None):
        if member is discord.Member.bot:
            return await ctx.send("Cannot fetch bot's info")
        member = ctx.author if not member else member
        time = member.created_at.strftime("%m/%d/%Y")
        roles = " ".join([role.mention for role in member.roles[1:]])
        #rolez = ",".join(roles)
        var = f"**Userinfo for {member.name}** \nName : {member} \nID : {member.id} \nRoles : {roles} \nAccount made : {time}"

        await ctx.send(f"{var}")


def setup(bot):
	bot.add_cog(Public(bot))

"""

"""