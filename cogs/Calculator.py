from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(aliases=['addition']) 
    async def add(self,ctx, *,nums):
      """ADD"""
      num_split = nums.split(',')
      operation = " + ".join(num_split)
      await ctx.send(f'{operation} = {eval(operation)}')
    
    @commands.command(aliases=['subtraction']) 
    async def sub(self,ctx, *,nums):
      """SUB"""
      num_split = nums.split(',')
      operation = " - ".join(num_split)
      await ctx.send(f'{operation} = {eval(operation)}')
    
    @commands.command(aliases=['multiplication']) 
    async def mul(self,ctx, *,nums):
      """MULTIPLY"""
      num_split = nums.split(',')
      operation = " * ".join(num_split)
      await ctx.send(f'{operation} = {eval(operation)}')

    @commands.command(aliases=['division']) 
    async def div(self,ctx, *,nums):
      """DIVIDE"""
      num_split = nums.split(',')
      operation = " / ".join(num_split)
      await ctx.send(f'{operation} = {eval(operation)}')

    @commands.command(aliases=['ave','aver']) 
    async def average(self, ctx, *, nums):
      """Average Finder"""

      nums_split = nums.split(',')
      num_send = ",".join(nums_split)
        
      for i in range(0, len(nums_split)):
        nums_split[i] = int(nums_split[i])
      
      operation = round(sum(nums_split) / len(nums_split), 3)
      await ctx.send(f'The Average of **{num_send}** is: ***{operation}***')

def setup(bot: commands.Bot): 
  bot.add_cog(Calculator(bot))

    


    



      
       

