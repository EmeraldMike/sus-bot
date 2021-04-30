import discord
from discord.ext import commands
from random import randrange
import os

DISCORD_TOKEN =''
PREFIX = '!'

sussy = commands.Bot(command_prefix=PREFIX)

@sussy.event 
async def on_ready():
	print("SUS CONNECTED TO SUSCORD! (100% imposter very sus no cap)")

@sussy.command()
async def sus(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
    susness = randrange(101)
    convertedsus = str(susness)
    convertedmember = str(member)
    embed=discord.Embed(title="SUSY BOTY", url="https://opensus.wtf", description=convertedmember + " is `" + convertedsus + "%` sus")
    embed.set_thumbnail(url="https://www.amonghelper.tk/among_us.png")
    embed.set_footer(text=ctx.message.author)
    await ctx.send(embed=embed)
@sussy.command()
async def imposter(ctx):
	await ctx.send('https://static.wikia.nocookie.net/jerma-lore/images/e/e3/JermaSus.jpg/revision/latest/top-crop/width/360/height/450?cb=20201206225609')

@sussy.command()
async def info(ctx):
	await ctx.send('SUS BOT by https://opensus.wtf ')

@sussy.command()
async def susimg(ctx):
    susy = randrange(9)
    convertedsusy = str(susy)
    embed=discord.Embed(title="SUSY BOTY", url="https://opensus.wtf", description="This image is pretty sus ngl")
    embed.set_thumbnail(url="https://opensus.wtf/assets/botimgs/" + convertedsusy + ".png")
    embed.set_footer(text=ctx.message.author)
    await ctx.send(embed=embed)
@sussy.command()
async def suscomit(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
    convertedmember = str(member)
    embed=discord.Embed(title="SUSY BOTY", url="https://opensus.wtf", description=convertedmember + " Has comited SUS")
    embed.set_thumbnail(url="https://opensus.wtf/assets/botimgs/thesus.png")
    await ctx.send(embed=embed)

sussy.run(DISCORD_TOKEN)
