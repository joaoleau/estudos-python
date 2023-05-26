from discord.ext import commands, tasks
import datetime

class Dates(commands.Cog):
    """Dates"""
    def __init__(self, bot):
       self.bot = bot

    @tasks.loop(seconds=10)
    async def current_time(self):
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y às %H:%M:%S")
        channel = self.bot.get_channel(1110650990815879258)
        await channel.send("Data atual: " + now)
    
async def setup(bot):
    await bot.add_cog(Dates(bot))
