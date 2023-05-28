from decouple import config
from discord.ext import commands
import discord
from discord import app_commands
import os
MY_GUILD = discord.Object(id=1110650990320963664)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

bot = commands.Bot(intents=intents, command_prefix="!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")
    await load_cogs(bot)
    synced = await bot.tree.sync(guild=MY_GUILD)
    print(f"Synced {len(synced)} command(s)")
    await bot.get_cog('Dates').current_time.start()
    

async def load_cogs(bot):
    for file in os.listdir("src/09-estudo-discord-bot/DiscordBot/commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f"commands.{cog}")
    await bot.load_extension("tasks.dates")
    await bot.load_extension("manager")


TOKEN = config("TOKEN")
bot.run(TOKEN)


