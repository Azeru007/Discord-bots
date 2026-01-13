import discord
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
async def mem1(ctx):
    with open("images/mem1.jpeg", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto twój mem, śmieszny co:", file=picture)

@bot.command()
async def mem2(ctx):
    with open("images/mem2.jpeg", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto twój mem, śmieszny co:", file=picture)

@bot.command()
async def mem3(ctx):
    with open("images/mem3.jpeg", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto twój mem, śmieszny co:", file=picture)

@bot.command()
async def mem(ctx):
    with open(f'images/{mem1}', 'rb') as f:
                picture = discord.File(f)


bot.run("MTQxNzU2NTIyMDkxODAwMTcxNA.GiUPzT.xwdyCK9iYh4-CRgWAEH8Ya9r0TeGbYJ3ZOsbog")