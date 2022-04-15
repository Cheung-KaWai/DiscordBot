import os
from dotenv import load_dotenv
from discord.ext import tasks, commands
import datetime

load_dotenv()

bot = commands.Bot(command_prefix="!")
global channel

@bot.event
async def on_ready():
  channel = bot.get_channel(729276302443413577)
  print("bot is ready")
  await channel.send("Alo")

@bot.command()
async def alo(ctx):
  await ctx.send("Konichiwa")

@bot.command()
async def vakantie(ctx):
  today = datetime.date.today()
  future = datetime.date(2022,6,24)
  diff = future - today
  await ctx.send(f"Nog {diff.days} dagen SIUUUUUUUUU")

bot.run(os.getenv('TOKEN'))