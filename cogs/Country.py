import requests
import discord
import asyncio
from discord.ext import commands

class Country(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=['ci','country'])
    async def country_info(self, ctx, *, country_search):
      """Country Info"""
      # async with ctx.typing():
      #   await asyncio.sleep(1)
      
      country_lower = country_search.lower()
      country_r = requests.get(f'https://restcountries.eu/rest/v2/name/{country_lower}?fullText=true')

      gmaps = f'https://www.google.com/maps/place/{country_lower}'
      
      country_name = (country_r.json()[0]['name'])
      country_alpha2Code = (country_r.json()[0]['alpha2Code'])
      country_alpha3Code = (country_r.json()[0]['alpha3Code'])
      country_callcode = (country_r.json()[0]['callingCodes'][0])
      country_capital = (country_r.json()[0]['capital'])
      country_region = (country_r.json()[0]['region'])
      country_subregion = (country_r.json()[0]['subregion'])
      country_population = (country_r.json()[0]['population'])
      country_demonym = (country_r.json()[0]['demonym'])
      country_area = (country_r.json()[0]['area'])
      country_timezone = (country_r.json()[0]['timezones'][0])
      country_currencycode = (country_r.json()[0]['currencies'][0]['code'])
      country_currencyname = (country_r.json()[0]['currencies'][0]['name'])
      country_currencysymbol = (country_r.json()[0]['currencies'][0]['symbol'])
      country_languagename = (country_r.json()[0]['languages'][0]['name'])
      country_languagenativename = (country_r.json()[0]['languages'][0]['nativeName'])
      
      country_flag_lower = country_alpha2Code.lower()

      embed = discord.Embed(title=country_name, colour=0x3498db)
      embed.add_field(name='Alpha2Code: ',value=country_alpha2Code,inline=True)
      embed.add_field(name='Alpha3Code: ',value=country_alpha3Code,inline=True)
      embed.add_field(name='Call Code: ',value=country_callcode,inline=True)
      embed.add_field(name='Capital: ',value=country_capital,inline=True)
      embed.add_field(name='Region: ',value=country_region,inline=True)
      embed.add_field(name='Sub Region: ',value=country_subregion,inline=True)
      embed.add_field(name='Population: ',value=country_population,inline=True)
      embed.add_field(name='Demonym: ',value=country_demonym,inline=True)
      embed.add_field(name='Area: ',value=f'{country_area} km²',inline=True)
      embed.add_field(name='Time Zone: ',value=country_timezone,inline=True)
      embed.add_field(name='Currency Name: ',value=country_currencyname,inline=True)
      embed.add_field(name='Currency Code: ',value=country_currencycode,inline=True)
      embed.add_field(name='Currency Symbol: ',value=country_currencysymbol,inline=True)
      embed.add_field(name='Language Name: ',value=country_languagename,inline=True)
      embed.add_field(name='Language Native Name: ',value=country_languagenativename,inline=True)
      embed.add_field(name='Google Maps: ',value=gmaps,inline=False)
      embed.set_image(url=f'https://flagcdn.com/160x120/{country_flag_lower}.png')

      await ctx.send(embed=embed)

def setup(bot: commands.Bot):
  bot.add_cog(Country(bot))

      
    



      
