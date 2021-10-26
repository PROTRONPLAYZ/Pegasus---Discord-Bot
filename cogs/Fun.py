import discord
import random
import requests
import time
import asyncio
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot
        self.last_msg = None

    @commands.command(aliases=["am_i_alive", "am_i_dead", "am_i_mix","is_protronplayz_alive","is_prot_alive", "mix", "dead"])
    async def alive(self, ctx):
      """This is made incase you think or confused if you are alive or not"""

      dead_life=["You are dead.... :(", "I am not sure about this one \nbut \nI think you are Dead...", "YOU ARE 100% DEAD..","You are alive right now but your death is coming soon... Get Ready"]
  
      alive_life=["You are alive.... :)","I am not sure about this one \nbut \nI think you are alive...","YOU ARE 100% ALIVE", "You are dead right now but you will be reborn in a few time... Get ready"]

      mix_life= ["OOSTANGBANGLA!!! \nFrom my test I have found that you are 50% Dead and 50% alive..."]

      all_life = [mix_life, dead_life, alive_life]

      test_ans = random.choice(all_life)

      if test_ans == alive_life:
     
        alive_embed=discord.Embed(title='Are you alive or dead???',description='This will test if you are alive or not...',colour=0x2ecc71)

        alive_embed.set_thumbnail(url="https://media.tenor.com/images/c0c571db482dc5d0a874f64f4b6d57a4/tenor.png")

        alive_embed.add_field(name='Dead or Alive Answer: ',value=random.choice(alive_life),inline=False)
        await ctx.send(embed=alive_embed)

      elif test_ans == dead_life:

        dead_embed=discord.Embed(title='Are you alive or dead???',description='This will test if you are alive or not...',colour=0xe74c3c)

        dead_embed.set_thumbnail(url="https://keralakaumudi.com/web-news/en/2020/11/NMAN0192759/image/dead-.1.836073.jpg")

        dead_embed.add_field(name='Dead or Alive Answer: ',value=random.choice(dead_life),inline=False)
        await ctx.send(embed=dead_embed)

      elif test_ans == mix_life:

        mix_embed=discord.Embed(title='Are you alive or dead???',description='This will test if you are alive or not...',colour=0x3498db)

        mix_embed.set_thumbnail(url="https://quotefancy.com/media/wallpaper/3840x2160/4946671-Dean-Koontz-Quote-I-m-alive-but-I-have-no-life-I-m-alive-but-also.jpg")

        mix_embed.add_field(name='Dead or Alive Answer: ',value=random.choice(mix_life),inline=False)
        await ctx.send(embed=mix_embed)

    @commands.command(aliases=["flip_a_coin", "toss"])
    async def flip(self, ctx):
      """Used for flipping a coin"""
      
      heads_1 = "It's Heads"
      heads_2 = "It's Heads"
      heads_3 = "It's Heads"
      tails_1 = "It's Tails"
      tails_2 = "It's Tails"


      all_toss = [heads_1,heads_2,heads_3,tails_1,tails_2]
      
      toss = random.choice(all_toss)

      if toss == heads_1:
        heads_1_embed=discord.Embed(title='Heads or Tails????',description='Lets see if the coin is heads or tails...',colour=0x3498db)

        heads_1_embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHrdgu0ZZbZVJFDhwGanN4YaVThOMGPNf5rw&usqp=CAU")

        heads_1_embed.add_field(name="Heads or Tails Ans: ",value=heads_1, inline=False)

        await ctx.send(embed=heads_1_embed)
      
      elif toss == heads_2:
        heads_2_embed=discord.Embed(title='Heads or Tails????',description='Lets see if the coin is heads or tails...',colour=0x3498db)

        heads_2_embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHrdgu0ZZbZVJFDhwGanN4YaVThOMGPNf5rw&usqp=CAU")

        heads_2_embed.add_field(name="Heads or Tails Ans: ",value=heads_2, inline=False)

        await ctx.send(embed=heads_2_embed)

      elif toss == heads_3:
        heads_3_embed=discord.Embed(title='Heads or Tails????',description='Lets see if the coin is heads or tails...',colour=0x3498db)

        heads_3_embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHrdgu0ZZbZVJFDhwGanN4YaVThOMGPNf5rw&usqp=CAU")

        heads_3_embed.add_field(name="Heads or Tails Ans: ",value=heads_3, inline=False)

        await ctx.send(embed=heads_3_embed)

      elif toss == tails_1:
        tails_1_embed=discord.Embed(title='Heads or Tails????',description='Lets see if the coin is heads or tails...',colour=0x3498db)

        tails_1_embed.set_thumbnail(url="https://qph.fs.quoracdn.net/main-qimg-6dd207e1e7d266fd3ffe6b0ae4f6ed73")

        tails_1_embed.add_field(name="Heads or Tails Ans: ",value=tails_1, inline=False)
        await ctx.send(embed=tails_1_embed)
      
      elif toss == tails_2:
        tails_2_embed=discord.Embed(title='Heads or Tails????',description='Lets see if the coin is heads or tails...',colour=0x3498db)

        tails_2_embed.set_thumbnail(url="https://qph.fs.quoracdn.net/main-qimg-6dd207e1e7d266fd3ffe6b0ae4f6ed73")

        tails_2_embed.add_field(name="Heads or Tails Ans: ",value=tails_2, inline=False)
        await ctx.send(embed=tails_2_embed)

    @commands.command(aliases=["j"])
    async def joke(self, ctx):
      """Joke Time!!!"""
      async with ctx.typing():
        await asyncio.sleep(1)

      joke_r=requests.get("https://icanhazdadjoke.com/slack")
      joke_json=(f"**{joke_r.json()['attachments'][0]['text']}**")

      joke_embed=discord.Embed(name='JOKE TIME',colour=0x3498db)

      joke_embed.set_thumbnail(url="https://static.toiimg.com/thumb/msid-75525287,imgsize-39184,width-800,height-600,resizemode-75/75525287.jpg")

      joke_embed.add_field(name='Joke: ',value=joke_json,inline=True)

      await ctx.send(embed=joke_embed)

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Get the bot's current websocket and API latency."""

        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")

    @commands.command(aliases=["quo","q"])
    async def quote(self, ctx):
      """If you are very discouraged then this will help you a lot"""

      async with ctx.typing():
        await asyncio.sleep(1)

      quotes_quote=requests.get(url="https://zenquotes.io/api/random")
      quotes_json= quotes_quote.json()

      quote=(f"*{quotes_json[0]['q']}*")
      quote_author=(f"\nThis quote was written by ***{quotes_json[0]['a']}***.")

      quote_embed=discord.Embed(title="These are quotes which will make your day...", description=f'***{"The quotes are told or written by many many famous people"}***',colour=0x3498db)

      quote_embed.set_thumbnail(url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/home-quotes-intro-1584721872.jpg?crop=0.502xw:1.00xh;0.250xw,0&resize=640:*")

      quote_embed.add_field(name="Quote: ", value=quote, inline=True)

      quote_embed.add_field(name="Author: ",value=quote_author, inline=True)

      await ctx.send(embed=quote_embed)

    # @commands.command(aliases=['poem','po'])
    # async def poems(self,ctx):
    #   pr = requests.get('')

    #   pr_title=(pr.json()[0: 154]['title'])

    #   await ctx.send(pr_title)

    @commands.command()
    async def copy(self,ctx,*,text):
      """This will copy you : )"""
      async with ctx.typing():
        await asyncio.sleep(1)
   
      await ctx.message.delete()
      await ctx.send(text)
      
    @commands.command(aliases=['ch'])
    async def choose(self,ctx,*,works):
    
      """If you are really confused among stuffs then this will help a lot"""

      async with ctx.typing():
        await asyncio.sleep(1)
         
      if " or " in works:
        delimiter = " or "
      elif ", " in works:
        delimiter = ", "
      else:
        delimiter = None

      if works != None:
        works_split= works.split(delimiter)
  
      work_send=random.choice(works_split)
      work_embed_send=f"***{work_send}***"
    
      if len(works_split) < 2:
        await ctx.send('I need 2 or more words for deciding')

      else:
        await ctx.reply(f'I say: {work_embed_send}', mention_author=True)

    @commands.command(aliases=['dice','roll_a_dice','rolladice'])
    async def roll(self,ctx):
      """Roll a dice"""

      dice1='https://upload.wikimedia.org/wikipedia/commons/2/2c/Alea_1.png'
      dice2='https://upload.wikimedia.org/wikipedia/commons/b/b8/Alea_2.png'
      dice3='https://upload.wikimedia.org/wikipedia/commons/2/2f/Alea_3.png'
      dice4='https://upload.wikimedia.org/wikipedia/commons/8/8d/Alea_4.png'
      dice5='https://upload.wikimedia.org/wikipedia/commons/5/55/Alea_5.png'
      dice6='https://upload.wikimedia.org/wikipedia/commons/f/f4/Alea_6.png'

      all_dice = [dice1, dice2, dice3, dice4, dice5,dice6]

      dice_embed=discord.Embed(colour=0x1abc9c)
      dice_embed.set_image(url=random.choice(all_dice))
      
      await ctx.send(embed=dice_embed)

    @commands.command(aliases=['ulta','rev'])
    async def reverse(self, ctx, *, text):
      """Incase You live in the mirror world lol."""
      await ctx.message.delete()
      await ctx.send(text[::-1])

    
   
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message

    @commands.command(aliases=['sn'])
    async def snipe(self, ctx):
      """Incase you are a spy and want to find out what a deleted msg said."""
      if not self.last_msg:
        await ctx.reply("EVEN WITH MY 999999 IQ I CANT SEE ANY MSG TO SNIPE!", mention_author = True)
      
      else: 
        name = self.last_msg.author.nick
        if name == None:
          name = self.last_msg.author.name

        content = self.last_msg.content
    
        embed = discord.Embed(title=f"Message from {name}",description=content)
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['s','annoy'])
    async def spam(self, ctx, *, word):
      """Used For Spamming"""
      await ctx.message.delete()
      if "," in word:
        delimiter = ","
      elif "|" in word:
        delimiter = "|"
      else:
        delimiter=None
      
      if delimiter != None:
        nums = word.split(delimiter)
      else:
        await ctx.send('```.spam|s|annoy {MSG} {, or |} {Number of times a msg to be repeated}```')
        return
      
      wordslst = nums[0]
      word_lst1 = int(nums[1])

      if word_lst1 > 100:
        await ctx.send("Sorry I can't spam that much :-(")
        await ctx.message.delete()

      else:
      
        for i in range(word_lst1):
          await ctx.send(wordslst)
          await asyncio.sleep(1)



def setup(bot: commands.Bot):
  bot.add_cog(Fun(bot))
    
