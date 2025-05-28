import discord
from discord.ext import commands
import os

# Bot token - replace with your actual token
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

# Initialize bot with command prefix
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# Remove the default help command
bot.remove_command('help')

# Load commands from different modules
async def load_commands():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"commands.{filename[:-3]}")
                print(f"Loaded extension: commands.{filename[:-3]}")
            except Exception as e:
                print(f"Failed to load extension commands.{filename[:-3]}: {e}")

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user.name}")
    await load_commands()

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)
