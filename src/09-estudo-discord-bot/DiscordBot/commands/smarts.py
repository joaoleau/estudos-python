from discord.ext import commands

class Smarts(commands.Cog):
    """A lot of Smart Commands"""
    def __init__(self, bot):
       self.bot = bot
    
    @commands.command(name="calcular", help="Calcula uma expressao")
    async def calculate_expression(self, ctx, *expression):
        expression = ''.join(expression) #'|'.join coloca os valores da tupla em uma unica str cujo sep='|'
        response = eval(expression)
        await ctx.send("A resposta é: " + str(response))
    
async def setup(bot):
    await bot.add_cog(Smarts(bot))
