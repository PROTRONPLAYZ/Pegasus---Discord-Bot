import discord
import requests
import random
import asyncio
from discord.ext import commands

class Space(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=["sp", 'space'])
    async def space_fact(self, ctx):
      """SPACE INFORMATION"""
      async with ctx.typing():
        await asyncio.sleep(1)

      space_info=requests.get(url="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=1")
      space_json_title=f"***{space_info.json()[0]['title']}***"
      space_json_info=f"*{space_info.json()[0]['explanation']}*"    
      space_json_date=f"*{'This picture was taken on'}* **{space_info.json()[0]['date']}**"    
      space_json_image=(space_info.json()[0]['url'])
      
      space_embed=discord.Embed(title='Space Info: ', colour=0x9b59b6)    
      space_embed.set_image(url=space_json_image)
      space_embed.add_field(name=space_json_title,value=space_json_info,inline=False)
      space_embed.add_field(name='Space Pic: ',value=space_json_date,inline=False)

      await ctx.send(embed=space_embed)

    @commands.command(aliases=['mars','rover'])
    async def mars_pics(self, ctx):
      mars_rand = random.randint(0, 855)
      mars_r = requests.get(url='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY')
      mars_r_pic = mars_r.json()['photos'][mars_rand]['img_src']
      
      await ctx.send(mars_r_pic)

def setup(bot: commands.Bot):
  bot.add_cog(Space(bot))

      
      