import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Wiki(Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Wiki(bot))
