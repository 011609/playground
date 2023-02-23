import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!!', intents=intents)

@bot.event
async def on_ready():
    print("Login:"+bot.user.display_name)

@bot.command()
async def 인사(ctx):
    await ctx.send("안녕!")

bot.run('어으 토큰 노출')