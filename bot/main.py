import discord
from discord.ext import commands
import os
import datetime

token = os.getenv("SCYLLA_TOKEN")

description = "A community driven Discord bot made for programmers, developers and hackers."
prefix = ">"
custom_status = prefix + "help"
bot = commands.Bot(command_prefix=prefix, description=description)

def initialize_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file{:-3}}")

def get_time():
    return datetime.now().strftime('%d/%m %H:%M:%S')

@bot.event
async def on_ready():
    print(f"[{get_time()}] Bot is online!")
    print(f"[{get_time()}] Logged in as {bot.user.name}")
    print(f"[{get_time()}] Setting status and activity")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(custom_status))
    print(f"[{get_time()}] Status set to {custom_status}")
    print(f"[{get_time()}] Initializing cogs")
    initialize_cogs()
    print(f"[{get_time()}] Cogs Initialized")
    print(f"[{get_time()}] Startup Complete")

try:
     bot.run(token)
except KeyboardInterrupt:
     bot.logout()