import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.utils import get
import random

bot = commands.Bot("-")

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	
@bot.command(aliases=['Hello','HELLO'])
async def hello(ctx):
	await ctx.message.delete()
	await ctx.send("Hello " + ctx.author.mention)
	
@bot.command(aliases=['SLAP','Slap'])
async def slap(ctx, user: discord.Member):
    if user is not None:
        await ctx.message.delete()
        embed=discord.Embed(description=ctx.message.author.mention + " just slapped the fuck out of " + "{} :wave:".format(user.name), color=discord.Color.blue())
        await ctx.send(embed=embed)
@bot.command()
async def embed(ctx, content:str, *, content1:str):
	await ctx.message.delete()
	embed = discord.Embed(title="{}".format(content), description="{}".format(content1), color=discord.Colour.green())
	await ctx.send(embed=embed)
@bot.command()
async def say(message, *, content:str):
	await message.channel.send(content)

bot.run('NTAxMTY1ODQxODU4MTY2Nzg2.DqVa4g.2bCjkj28NqQ96CfeKGk5fIR36OQ')
