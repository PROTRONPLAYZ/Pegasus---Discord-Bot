import requests
import asyncio
from discord.ext import commands

class Money(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=["con", "convert"])
    async def money_con(self, ctx, money: int,*,currencies):
    
      """Convert Any Currency to Any Currency with any amount"""
      async with ctx.typing():
        await asyncio.sleep(1)
      
      cur_r = requests.get('http://data.fixer.io/api/latest?access_key=07053bdc5390aeafa2f8ed39b71a12fa')
      
      currency_list = currencies.split(' to ')

      currency1 = currency_list[0]
      currency2 = currency_list[1]  
      
      currency1_lower = currency1.upper()
      currency2_lower = currency2.upper()

      cur1_rate = (cur_r.json()['rates'][currency1_lower])
      cur2_rate = (cur_r.json()['rates'][currency2_lower])

      cur_convert=  round(cur2_rate / cur1_rate * money)

      cur_send = f'**{money}** *{currency1}* is **{cur_convert}** *{currency2}*'

      await ctx.send(cur_send)

def setup(bot: commands.Bot):
  bot.add_cog(Money(bot))

