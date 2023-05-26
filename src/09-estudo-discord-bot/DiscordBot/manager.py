from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """Manager"""
    def __init__(self, bot):
       self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "palavrao" in message.content:
            await message.channel.send(f"Por favor, {message.author.name}, nao ofenda os demais usuarios!")
            await message.delete()
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send("Favor enviar todos os argumentos. Digite !help para ver comandos")
        if isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Digite !help para ver comandos")
        else:
            raise error
    
async def setup(bot):
    await bot.add_cog(Manager(bot))
