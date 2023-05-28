from discord.ext import commands
import discord
from discord import app_commands
MY_GUILD = discord.Object(id=1110650990320963664)

class Images(commands.Cog):
    """Works with images"""
    def __init__(self, bot):
       self.bot = bot
    
    @app_commands.command(name="foto", description="Cria uma foto aleatoria")
    async def get_random_image(self, interaction:discord.Interaction):
        url_image = "https://picsum.photos/1920/1080"

        embed = discord.Embed(
            title = "Resultado da Busca",
            description = "Busca aleatoria",
            color = 0x0000FF
        )

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.set_footer(text="Feito por: ", icon_url=self.bot.user.avatar)
        embed.set_image(url=url_image)
        
        embed.add_field(name="API", value="Usamos a API do: https://picsum.photos/1920/1080 ")
        embed.add_field(name="Parametros", value="{largura}/{altura}")
        embed.add_field(name="Exemplo", value=url_image, inline=False)
        await interaction.response.send_message(embed=embed)

    
async def setup(bot):
    await bot.add_cog(Images(bot), guilds=[MY_GUILD])
