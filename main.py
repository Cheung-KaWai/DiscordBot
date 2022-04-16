import os
from dotenv import load_dotenv
from discord.ext import tasks, commands
import datetime, asyncio,requests,json

load_dotenv()

bot = commands.Bot(command_prefix="!")
vacation = datetime.date(2022,6,24)
links=json.load(open("gifs.json"))

def getDays():
  today = datetime.date.today()
  diff = vacation - today
  return diff.days

async def schedule_daily_message():
  while True:
    now = datetime.datetime.now()
    then = now + datetime.timedelta(days=1)
    then.replace(hour=8,minute=0)
    wait_time=(then-now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = bot.get_channel(729276302443413577)

    await channel.send(f"nog {getDays()} dagen SIUUUUUUUUU")
    await channel.send(links["gif"])


@bot.command()
async def alo(ctx):
  await ctx.send("Konichiwa")

@bot.command()
async def vakantie(ctx):
  await ctx.send(f"Nog {getDays()} dagen SIUUUUUUUUU")

@bot.event
async def on_ready():
  channel = bot.get_channel(729276302443413577)
  print("bot is ready")
  await channel.send("Alo SIUUUUUUUUU")
  await schedule_daily_message()

bot.run(os.getenv('TOKEN'))