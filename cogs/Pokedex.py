import discord
import requests
from discord.ext import commands

class Pokedex(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=['poke','pokemon'])
    async def pokedex(self, ctx,*,Pokemon):
      """Pokedex INCASE YOU ARE A POKEMON FANNNN!!!"""
      Poke_Url = requests.get(url=f'https://pokeapi.co/api/v2/pokemon/{Pokemon}')
      Poke_BaseEx=(Poke_Url.json()['base_experience'])
      Poke_height=(Poke_Url.json()['height'])
      Poke_weight=(Poke_Url.json()['weight'])

      embed=discord.Embed(title='Pokedex',description='Info of Pokemons', colour=0x1abc9c)
      embed.add_field(name='Name: ',value=Pokemon,inline=False)
      embed.add_field(name='Base Exp: ',value=f'{Poke_BaseEx} exp',inline=False)
      embed.add_field(name='Height: ',value=Poke_height,inline=False)
      embed.add_field(name='Weight: ',value=Poke_weight,inline=False)
      embed.set_image(url=f'https://play.pokemonshowdown.com/sprites/xyani/{Pokemon}.gif')
      
      await ctx.send(embed=embed)

def setup(bot: commands.Bot):
  bot.add_cog(Pokedex(bot))


