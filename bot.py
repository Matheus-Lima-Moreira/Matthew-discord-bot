import os
import discord
from decouple import config
from discord.ext import commands

activity = discord.Activity(type=discord.ActivityType.listening, name="mtw!help")
bot      = commands.Bot(command_prefix="mtw!", activity=activity, status=discord.Status.idle)

def load_cogs(bot):
    bot.load_extension('manager')

    for file in os.listdir('commands'):
        if file.endswith('.py'):
            cog = file[:-3]
            bot.load_extension(f'commands.{cog}')

    bot.load_extension('tasks.dates')

load_cogs(bot)

TOKEN = config('TOKEN')
bot.run(TOKEN)