import os
import discord
from discord.ext import commands, tasks
import socket
import random
from alive import alive
from quote import quote
from datetime import datetime
import asyncio
import aiohttp, json

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(intents = intents, command_prefix=["//"], allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False))
time = datetime.now().strftime("%H:%M:%S")

async def quote_gen():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://zenquotes.io/api/random") as response:
            json_data = json.loads(await response.text())
            quote = json_data[0]["q"]
            return quote
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game(name='with Marin & everyone || type //help'))
@tasks.loop(seconds=86400)
async def quoter():
    await bot.wait_until_ready()
    quotes = await quote_gen()
    channel = bot.get_channel(945473529493725294) # channel ID goes here
    while not bot.is_closed():
        try: 
            await channel.send(quotes)
            await asyncio.sleep(86400)
        except:
            pass
    bg_task = bot.loop.create_task(quoter())


alive()
for filename in os.listdir('src/main/python/org/CloverBot'):
    if filename.endswith('.py'):
        bot.load_extension(f'src.main.python.org.CloverBot.{filename[:-3]}')
bot.run(os.environ["token"])
