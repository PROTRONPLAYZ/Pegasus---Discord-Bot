import random
import asyncio
from discord.ext import commands

class Eightball(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=['8ball','8b','ball'])
    async def eiball(self, ctx,*,questions):
      """8ball Just Like Every Other Bots Have : )"""
      async with ctx.typing():
        await asyncio.sleep(1)

      if ctx.author.nick == None:
        name=ctx.author.name
      else:
        name=ctx.author.nick

      responses=[
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes - definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"]
      send_ans = random.choice(responses)
        
      await ctx.reply(f"🎱 {send_ans}, ***{name}**", mention_author=True)

def setup(bot: commands.Bot):
  bot.add_cog(Eightball(bot))
