# bot.py
from discord.ext import commands
import sp2_picker as sp2p
import sys

bot = commands.Bot(command_prefix='!')

@bot.command()
async def pick(ctx, *args):
    argList = []
    for arg in args:
        argList.append(arg)
    listArr = sp2p.pick(*argList)
    i=0
    for arg in args:
        await ctx.send((str(arg) + ': ' + str(listArr[i])))
        i+=1

bot.run('your-bot-token')
