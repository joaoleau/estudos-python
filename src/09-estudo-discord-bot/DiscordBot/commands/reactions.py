from discord.ext import commands

class Reactions(commands.Cog):
    """Works with reactions"""
    def __init__(self, bot):
       self.bot = bot
    
    # events -> commands.Cog.listener
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == '👍':
            role = user.guild.get_role(1111416243879153806)
            await user.add_roles(role)
        elif reaction.emoji == '💩':
            role = user.guild.get_role(1111416324925702174)
            await user.add_roles(role)
    


async def setup(bot):
    await bot.add_cog(Reactions(bot))
