import discord
import lichess.api
from discord.ext import commands

class Lichess(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=['update'])
    async def profile(self, ctx, member: discord.Member):
      """Lichess Profiles but its still underdevelopment : ("""
      if member == None:
        user = lichess.api.user(ctx.author)
      else:
        user = lichess.api.user(member)
      
      rapid = (user['perfs']['rapid']['rating'])
      blitz = (user['perfs']['blitz']['rating'])
      bullet = (user['perfs']['bullet']['rating'])

      await ctx.send(f'Rapid: **{rapid}** \nBlitz: **{blitz}**\nBullet: **{bullet}**')

def setup(bot: commands.Bot):
  bot.add_cog(Lichess(bot))



 