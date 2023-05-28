from discord.ext import commands
import discord
from discord import app_commands
MY_GUILD = discord.Object(id=1110650990320963664)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

class Talks(commands.Cog):
    """ Fala com o usuario """

    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def sync(self, ctx) -> None:
    #     fmt = await ctx.bot.tree.sync(guild=ctx.guild)
    #     await ctx.send(f"Synced {len(fmt)} commands")

    @app_commands.command(name='oi', description="Manda um oi")
    async def send_hi(self, interaction: discord.Interaction):
        name = interaction.user.name
        response = 'Salve, ' + name
        await interaction.response.send_message(response)

    @app_commands.command(name="segredo", description="Manda um segredo no pv")
    async def secret(self, interaction: discord.Interaction):
        try:
            await interaction.response.send_message("SEGREDOOOO")
        except discord.errors.Forbidden:
            await interaction.response.send_message("Não posso te contar o segredo, habilite a opção para receber mensagem no privado.")


async def setup(bot):
    await bot.add_cog(Talks(bot), guilds=[MY_GUILD])