import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def punch(self, user : discord.Member):
        """i will puch anyone!!"""

        #Your code will go here
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

def setup(bot):
    bot.add_cog(Mycog(bot))
