import requests
from discord.ext import commands

class Pics(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=["koa"])
    async def koala(self, ctx):
      """KOALA PICS"""
      koala_pic=requests.get(url="https://some-random-api.ml/img/koala")
      koala_json= koala_pic.json()

      await ctx.send(koala_json['link'])

    @commands.command(aliases=["pan"])
    async def panda(self, ctx):
      """PANDA PICS"""

      panda_pic=requests.get(url="https://some-random-api.ml/img/panda")
      panda_json= panda_pic.json()

      await ctx.send(panda_json['link'])

    @commands.command(aliases=['rpan','rp'])
    async def red_panda(self, ctx):
      """RED PANDA PICS (YES THERE IS A HUGE DIFFERENCE BETWEEN RED PANDAS AND PANDAS)"""
      redpanda_pic=requests.get(url='https://some-random-api.ml/img/red_panda')
      redpanda_json=redpanda_pic.json()

      await ctx.send(redpanda_json['link'])

    @commands.command(aliases=["b"])
    async def bird(self, ctx):
      """BIRD PICS"""
      bird_pic=requests.get(url="https://some-random-api.ml/img/birb")
      bird_json= bird_pic.json()

      await ctx.send(bird_json['link'])

    @commands.command(aliases=["pika"])
    async def pikachu(self, ctx):
      """PIKACHU GIFS"""
      pika_pic=requests.get(url="https://some-random-api.ml/img/pikachu")
      pika_json= pika_pic.json()

      await ctx.send(pika_json['link'])
    
    @commands.command(aliases=["meow"])
    async def cat(self, ctx):
      """CAT PICS"""
      cat_pic=requests.get(url="https://api.thecatapi.com/v1/images/search")
      cat_json= (cat_pic.json()[0]['url'])

      await ctx.send(cat_json)
    
    @commands.command(aliases=["woof"])
    async def dog(self, ctx):
      """DOG PICS"""
      dog_pic=requests.get(url="https://api.thedogapi.com/v1/images/search")
      dog_json= dog_pic.json()[0]['url']

      await ctx.send(dog_json)

    @commands.command(aliases=["mon"])
    async def monkey(self, ctx):
      """MONKEY PICS"""

      await ctx.send("https://www.placemonkeys.com/500/350?random")

    


def setup(bot: commands.Bot):
  bot.add_cog(Pics(bot))
