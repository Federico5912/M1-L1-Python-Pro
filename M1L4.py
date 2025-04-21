#Bot
import discord
from discord.ext import commands
import os
import random
# Cargar variables de entorno
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am your bot!')
@bot.command()
async def dado(ctx, caras: int = 6):
    resultado = random.randint(1, caras)
    await ctx.send(f'🎲 Has lanzado un dado de {caras} caras y salió: {resultado}')
# Obtener token de variables de entorno
bot.run('TOKEN')
