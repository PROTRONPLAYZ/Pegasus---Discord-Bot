import discord
import requests
import asyncio
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=["cf"])
    async def cat_fact(self, ctx):
      """CAT FACT"""
      async with ctx.typing():
        await asyncio.sleep(1)
      
      cat_pic = requests.get("https://some-random-api.ml/img/cat")
      cat_pic_send = (cat_pic.json()['link'])
      
      cat_res = requests.get("https://some-random-api.ml/facts/cat")
      cat_json = cat_res.json()
      cat_send = (cat_json['fact'])
      
      cat_embed=discord.Embed(title='This is a cat fact', colour=0x7289da)

      cat_embed.set_image(url=cat_pic_send)

      cat_embed.add_field(name="Cat Fact: ", value=f'***{cat_send}***',inline=True)

      await ctx.send(embed=cat_embed)

    @commands.command(aliases=["df"])
    async def dog_fact(self, ctx):
      """DOG FACT"""
      async with ctx.typing():
        await asyncio.sleep(1)

      dog_pic = requests.get("https://dog.ceo/api/breeds/image/random")
      dog_pic_json= (dog_pic.json()['message'])
      
      dog_res = requests.get("https://some-random-api.ml/facts/dog")
      dog_json = dog_res.json()
      dog_send = (dog_json['fact'])
      
      dog_embed=discord.Embed(title='This is a dog fact', colour=0x7289da)

      dog_embed.set_image(url=dog_pic_json)

      dog_embed.add_field(name="Dog Fact: ", value=f'***{dog_send}***',inline=True)

      await ctx.send(embed=dog_embed)

    @commands.command(aliases=["kf"])
    async def koala_fact(self, ctx):
      """KOALA FACT"""
      async with ctx.typing():
        await asyncio.sleep(1)
      
      koa_res = requests.get("https://some-random-api.ml/facts/koala")
      koa_json = (koa_res.json()['fact'])
      
      koa_embed=discord.Embed(title='This is a koala fact', colour=0x7289da)

      koa_embed.add_field(name="Koala Fact: ", value=f'***{koa_json}***',inline=True)

      await ctx.send(embed=koa_embed)


def setup(bot: commands.Bot):
  bot.add_cog(Info(bot))