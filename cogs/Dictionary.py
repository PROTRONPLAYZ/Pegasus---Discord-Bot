import discord
import requests
import asyncio
from discord.ext import commands

class Dictionary(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=['dict'])
    async def dictionary(self, ctx, *,word):
      """Incase you are lazy to use Google Dictionary"""
      async with ctx.typing():
        await asyncio.sleep(1)
      
      Audio_Upper = word.lower()
      
      dic_api = requests.get(url=f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}")

      dic_meaning = (dic_api.json()[0]['meanings'][0]['definitions'][0]['definition'])

      dic_text = (dic_api.json()[0]['phonetics'][0]['text'])

      dic_partsofspeech = (dic_api.json()[0]['meanings'][0]['partOfSpeech'])

      dic_example = (dic_api.json()[0]['meanings'][0]['definitions'][0]['example'])

      dic_audio=f"https://lex-audio.useremarkable.com/mp3/{Audio_Upper}_us_1.mp3"

      embed = discord.Embed(title='Dictionary', colour=0x3498db)
      embed.add_field(name='Word: ', value=f'**{word}**', inline=False)
      embed.add_field(name='Pronounciation: ', value=f'{dic_text}', inline=False)
      embed.add_field(name='Meaning: ', value=f'*{dic_meaning}*', inline=False)
      embed.add_field(name='Parts Of Speech: ', value=f'*{dic_partsofspeech}*', inline=False)
      embed.add_field(name='Example: ', value=f'***{dic_example}***', inline=False)
      embed.add_field(name='Audio: ', value=dic_audio, inline=False)

      await ctx.send(embed=embed)

def setup(bot: commands.Bot):
  bot.add_cog(Dictionary(bot))

 