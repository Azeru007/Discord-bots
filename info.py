import discord
from os import listdir
from random import choice
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    images = listdir("images")
    with open(f"images/{choice(images)}", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto twój mem, śmieszne co:", file=picture)


bot.run("MTQxNzU2NTIyMDkxODAwMTcxNA.GiUPzT.xwdyCK9iYh4-CRgWAEH8Ya9r0TeGbYJ3ZOsbog")