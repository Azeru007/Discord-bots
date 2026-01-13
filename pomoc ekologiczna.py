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
async def pomoc(ctx):
    with open("images/pomoc.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def pytanie1(ctx):
    with open("images/pytanie1.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto odpowiedź na pierwsze pytanie:", file=picture)

@bot.command()
async def pytanie2(ctx):
    with open("images/pytanie2.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto odpowiedź na pierwsze pytanie:", file=picture)

@bot.command()
async def pytanie3(ctx):
    with open("images/pytanie3.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto odpowiedź na pierwsze pytanie:", file=picture)

@bot.command()
async def pytanie4(ctx):
    with open("images/pytanie4.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto odpowiedź na pierwsze pytanie:", file=picture)

@bot.command()
async def pytanie5(ctx):
    with open("images/pytanie5.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto odpowiedź na pierwsze pytanie:", file=picture)

@bot.command()
async def pytanie6(ctx):
    with open("images/pytanie6.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto odpowiedź na pierwsze pytanie:", file=picture)

@bot.command()
async def pytanie7(ctx):
    with open("images/pytanie7.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto odpowiedź na pierwsze pytanie:", file=picture)

@bot.command()
async def pytanie8(ctx):
    with open("images/pytanie8.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto odpowiedź na pierwsze pytanie:", file=picture)

@bot.command()
async def pytanie9(ctx):
    with open("images/pytanie9.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto odpowiedź na pierwsze pytanie:", file=picture)

@bot.command()
async def pytanie10(ctx):
    with open("images/pytanie10.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send("Oto odpowiedź na pierwsze pytanie:", file=picture)

bot.run("")
