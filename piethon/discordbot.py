import discord
from discord.ext import commands

TOKEN = 'YOUR TOKEN'
guild = ['my', 'guild', 'ids']

bot = discord.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('---------------------')
    print('BOT IS ONLINE')
    print(f'NAME : {bot.user.name}')
    print(f'ID : {bot.user.id}')
    print(f'SERVER JOINED : {str(len(bot.guilds))}')
    print('---------------------')
    await bot.change_presence(activity=discord.Game(name="✨gomteng#0693✨"))

@bot.command()
async def ping(ctx):
    ctx.send(f'Pong! {bot.latency}')

@bot.command()
async def reaction(ctx):
    await ctx.message.add_reaction('😋')

@bot.slash_command(description="bot's slash command", guild_ids=guild)
async def greeting(ctx, name):
    ctx.respond(f'Hello {name}!')

bot.run(TOKEN)