from discord.ext import commands
import discord

class Talks(commands.Cog):
    """Talks with user"""
    def __init__(self, bot):
       self.bot = bot
    
    # ctx contexto
    @commands.command(name="oi", help="Envia um Oi (Nao requer arg)") #Nome do comando oi; !oi retorna isso ai
    async def send_hello(self, ctx):
        name = ctx.author.name
        response = "Ola, " + name
        await ctx.send(response)

    @commands.command(name="segredo", help="Conta um segredo no seu pv")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Segredo!")
        except discord.errors.Forbidden:
            await ctx.send("Sem permissao para contar o segredo")

async def setup(bot):
    await bot.add_cog(Talks(bot))
