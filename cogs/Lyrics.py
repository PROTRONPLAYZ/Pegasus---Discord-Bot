import lyricsgenius
import asyncio
from discord.ext import commands

class Lyrics(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=['lyrics'])
    async def lyric(self,ctx,*,song):
      """Song lyrics"""
      async with ctx.typing():
        await asyncio.sleep(1)
      genius = lyricsgenius.Genius('GENIUS_ACCESS_TOKEN')
   
      input_song = genius.search_song(song)
      song_send = input_song.lyrics
      if len(song_send) > 2000:
        song_list = song_send.split(' ')
        song_send1= ' '.join(song_list[:200])
        await ctx.send(f'```{song} lyrics: \n\n {song_send1}```')
        await ctx.send("You can find the whole lyrics on {idk}")

      else:
        await ctx.send(f'```{song} lyrics: \n\n {song_send} ```')
        await ctx.send("You can find the whole lyrics on {idk}")

def setup(bot: commands.Bot):
  bot.add_cog(Lyrics(bot))