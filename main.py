import discord  
import os
import asyncio
import random
from Keep_Alive import Keep_Alive
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('.', '. '), activity=discord.Game(name=".help"))

bot.load_extension('cogs.Fun')
bot.load_extension('cogs.Info')
bot.load_extension('cogs.Pics')
bot.load_extension('cogs.Calculator')
bot.load_extension('cogs.Lyrics')
bot.load_extension('cogs.Dictionary')
bot.load_extension('cogs.Money')
bot.load_extension('cogs.Chess')
bot.load_extension('cogs.8ball')
bot.load_extension('cogs.Pokedex')
bot.load_extension('cogs.Country')
bot.load_extension('cogs.Space')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# @bot.event
# async def on_command_error(ctx, error):
#   await ctx.reply(f"Ahh I dont know what you are trying to say <:OhGodOhNo:836482963344457728>  \nType **{'.help'}** to get more info",mention_author=True)

@bot.event
async def on_member_join(ctx, member):
    print(f'{member} has joined a server.')

    await ctx.send(f"Hello {member}!")
    await member.send(f'Hello {member}! I am a bot so that means I always help you....anyways there are some rules to follow so you must follow them or you DIE.. LOL just kidding.. \nSo the rules are \nNo pinging anyone unless its important \n No Talking Rubbish (like I do most of the times) \n NO SMOKING \n NO KICKING ANYONE (OF COURSE YOU CANT DO THAT BCAUSE I RULE THE SERVER : )) \nAND LAST BUT NOT THE LEAST::: NO ANNOYING ANYONE OK???, IF NO; Then IDK.')

@bot.command(aliases=['hello','bello'])
async def hi(ctx):
  """Just Used for Greetings"""
  async with ctx.typing():
        await asyncio.sleep(1)

  if ctx.author.nick == None:
    name=ctx.author.name
  else:
    name=ctx.author.nick

  embed=discord.Embed(
        title=f"Hello **{name}**, I am {bot.user.name}!...\nNice to meet you. I will be always at your help....  :grin:" ,colour=0x3498db)      
  embed.set_thumbnail(url=bot.user.avatar_url
   )     
  await ctx.send(embed=embed)

@bot.command(aliases=['tata','BYE'])
async def bye(ctx):
  """Just used for saying bye in a formal manner"""     
  embed=discord.Embed(
        title=f"Bye...have a nice day\n....  :wave:" ,colour=0x3498db)

  embed.set_thumbnail( url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVdosJvPeezKKg0MNat7etXwvhqgeTeh2WTg&usqp=CAU"
  )      
  await ctx.send(embed=embed)

@bot.command(aliases=['Gn', 'gN', 'GN', 'Good_Night'])
async def gn(ctx):
  """Good Nights"""
  await ctx.send(f'Good Night')

@bot.command(aliases=['Gm', 'gM', 'GM', 'Good_Morning'])
async def gm(ctx):
  """Good Mornings"""
  await ctx.send('Good Morning')

@bot.command(aliases=['thx'])
async def thanks(ctx):
  """Just for saying thanks to my bot"""
  all_thx = ['No Problem', 'Always at your service', "I don't like to help you sometimes lol", 'Ahh its okay', "I am very sleep now so don't ask me any help if you want any help ask @Coeus"]

  thx_send=random.choice(all_thx)

  await ctx.send(thx_send)

@bot.command(aliases=['p'])
async def purge(ctx, amount: int):
  """It can delete msgs upto 100"""
  # if int == False:
  #   await ctx.send("You have to type in this format \n```.purge {Number of messages you want to delete```")

  if amount > 100:
    await ctx.send('OMG I cant do that. Because if I try to do it I will be like this guy :point_right: :exploding_head: ')
  else:  
    await ctx.channel.purge(limit=amount + 1)
  
    name = ctx.author.nick
    if name == None:
      name = ctx.author.name
    
    if amount==1:
      await ctx.send(f"**{amount}** message were deleted by **{ctx.author.name}**", delete_after = 1.5)
    
    else:
     await ctx.send(f"**{amount}** messages were deleted by **{ctx.author.name}**", delete_after = 1.5)

@bot.command(aliases=['srv'])
async def servers(ctx):
  """None of your business"""
  servers=str(len(bot.guilds))

  embed=discord.Embed(title='NUMBER OF SERVERS THAT I EXIST', description=f'I Live In {servers} Servers.',colour=0x1abc9c)
  embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/781921132591972402.png?v=1')
  await ctx.send(embed=embed)

@bot.command(aliases=['ui','usinf'])
async def user_info(ctx, member: discord.Member):
  """User Information like Joined Discord, Nickname Etc."""
  # if member.nick == None:
  #   nick='This User is Nick Name Less'
  # else:
  #   nick=member.nick
  
  if member == None:
    if ctx.nick == None:
      nick='This User is Nick Name Less'
    else:
      nick=ctx.nick

    embed=discord.Embed(title='User Info :book:', colour=0x1abc9c)
    embed.add_field(name='User Name: ', value=ctx, inline=False)
    embed.add_field(name='User id: ', value=ctx.id, inline=False)
    embed.add_field(name='Joined Discord: ',value=ctx.created_at,inline=False)
    embed.add_field(name='Nick Name: ',value=nick)
    #embed.add_field(name='HypSquad: ',value=member.hypesquad_bravery,inline=False)
    embed.set_image(url=ctx.avatar_url)

    await ctx.send(embed=embed)

  else:
    if member.nick == None:
      nick='This User is Nick Name Less'
    else:
      nick=member.nick
  
    embed=discord.Embed(title='User Info :book:', colour=0x1abc9c)
    embed.add_field(name='User Name: ', value=member, inline=False)
    embed.add_field(name='User id: ', value=member.id, inline=False)
    embed.add_field(name='Joined Discord: ',value=member.created_at,inline=False)
    embed.add_field(name='Nick Name: ',value=nick)
    #embed.add_field(name='HypSquad: ',value=member.hypesquad_bravery,inline=False)
    embed.set_image(url=member.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def nick(ctx, member: discord.Member,nick):
  """Used for changing nick"""

  member = ctx.author
  
  await member.edit(nick=nick)
  await ctx.reply(f'You Nick Has Been Changed To **{nick}**', mention_author=True)

@bot.command()
async def dm(ctx, member: discord.User, *, msg):
  """DMING PPL"""
  await member.send(msg)

Keep_Alive()
bot.run(os.getenv('PEGASUS'))





