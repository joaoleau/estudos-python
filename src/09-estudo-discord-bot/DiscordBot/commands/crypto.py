from discord.ext import commands
import requests
import discord
from discord import app_commands
MY_GUILD = discord.Object(id=1110650990320963664)

class Crypto(commands.Cog):
    """Works with Cryptocurrency"""
    def __init__(self, bot):
       self.bot = bot
    
    @app_commands.command(name="binance", description="Compara valores monetarios")
    async def binance(self, interaction: discord.Interaction, coin:str, base:str):
        
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get("price")
            if price:
                await interaction.response.send_message(f"O valor do {coin}/{base} é {price}")
            else:
                await interaction.response.send_message(f"O par {coin}/{base} é invalido")
        except Exception as error:
            await interaction.response.send_message("Deu algum erro")
            print(error)
    
async def setup(bot):
    await bot.add_cog(Crypto(bot), guilds=[MY_GUILD])
