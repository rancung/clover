from discord.ext import commands
import discord
import urllib
import random
import aiohttp
import session
import requests
import animec
from aiohttp import ClientSession

async def get(session: object, url: object) -> object:
    async with session.get(url) as response:
        return await response.text()

class Funs(commands.Cog):
    def __init__(self, bot):
        self.author = None
        self.bot = bot
    @commands.group(invoke_without_command=True)
    async def cat(self, ctx):
        response = requests.get('https://aws.random.cat/meow')
        data = response.json()
        const = discord.Embed(title="About Cat", description="`Felis catus` or known as `Cat` is a domestic species of a small carnivorous mammal. It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from the wild members of the family.", color=0x400080)
        const.set_thumbnail(url=data['file'])
        await ctx.send(embed=const)
    @cat.command(aliases=["img","pict"])
    async def image(self, ctx):
        response = requests.get('https://aws.random.cat/meow')
        data = response.json()
        embed=discord.Embed(title="Random Cat", color=0x400080)
        embed.set_image(url=data['file'])
        await ctx.send(embed=embed)
    @cat.command()
    async def fact(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://catfact.ninja/fact") as response:
                fact = (await response.json())["fact"]
                length = (await response.json())["length"]
                embed = discord.Embed(title=f'Random Cat Fact Number: **{length}**', description=f'Cat Fact: {fact}', colour=0x400080)
                embed.set_footer(text="")
                await ctx.send(embed=embed)
      # await session.close() # <--- here, but is not necessary
    @commands.command()
    async def say(self, ctx, word: str=None):
        if word is None:
            await ctx.send("Write the word you stupid fools")
            return
        embed = discord.Embed(description=f"{ctx.author.name} \n{word}"        )
        await ctx.send(embed=embed )

    @commands.command()
    async def anime(self, ctx, animex:str):
        try:
            anime=animec.Anime(animex)
        except:
            await ctx.send("Something went wrong, please try again later")
        const = discord.Embed(title=anime.name, url=anime.url, description=anime.description, color=0x400080)
        const.add_field(name="Rank", value=str(anime.ranked))
        const.add_field(name="Episode", value=str(anime.episodes))
        const.add_field(name="Statuses", value=str(anime.status))
        const.add_field(name="Anime Type", value=str(anime.type))
        const.add_field(name="Popularity", value=str(anime.favorites))
        const.set_thumbnail(url=anime.poster)
        await ctx.send(embed=const)


        
        

def setup(bot):
    bot.add_cog(Funs(bot))