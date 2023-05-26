from discord.ext import commands
import requests

class Crypto(commands.Cog):
    """Works with Cryptocurrency"""
    def __init__(self, bot):
       self.bot = bot
    
    @commands.command(name="binance", help="Compara valores monetarios")
    async def binance(self, ctx, coin, base):
        
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get("price")
            if price:
                await ctx.send(f"O valor do {coin}/{base} é {price}")
            else:
                await ctx.send(f"O par {coin}/{base} é invalido")
        except Exception as error:
            await ctx.send("Deu algum erro")
            print(error)
    
async def setup(bot):
    await bot.add_cog(Crypto(bot))
