import random

countryFile = open('sp2_countries.txt', 'r')
countryList = countryFile.readlines()
numPlayers = input('insert number of players: ')

allchosen = []
for player in range(int(numPlayers)):
    chosen = []
    for i in range(0, 10):
        choice = countryList[random.randint(0, len(countryList)-2)]
        truth = True
        while truth:
            if(choice in chosen or choice in allchosen):
                choice = countryList[random.randint(0, len(countryList)-2)]
            else:
                truth = False
                chosen.append(choice[0:len(choice)-1])
                allchosen.append(choice[0:len(choice)-1])
    print(chosen)