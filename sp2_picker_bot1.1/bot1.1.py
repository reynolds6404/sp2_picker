from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.command()
async def pick2(ctx, *args):
    countryFile = open('sp2_countries.txt', 'r')
    countryList = countryFile.readlines()

    allchosen = []
    numArgs = len(args)
    numCountries = 10
    if (numArgs > 18):
        numCountries = 5
    for arg in args:
        chosen = []
        for i in range(0, numCountries):
            choice = countryList[random.randint(0, len(countryList)-1)]
            truth = True
            while truth:
                if(choice[0:len(choice)-1] in chosen) or (choice[0:len(choice)-1] in allchosen):
                    choice = countryList[random.randint(0, len(countryList)-1)]
                else:
                    truth = False
                    chosen.append(choice[0:len(choice)-1])
                    allchosen.append(choice[0:len(choice)-1])
        await ctx.send((str(arg) + ':\n' + ('\n'.join(map(str, chosen)))))

bot.run('NzA1Nzg0MzEzNDg4MjEyMDY5.XqwxQw.zVNBnio607MeEh1YS3tsO-zAzwQ')
