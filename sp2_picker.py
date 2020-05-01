import random

countryFile = open('sp2_countries.txt', 'r')
countryList = countryFile.readlines()

def pick(*args):
    allchosen = []
    listArr = []
    for arg in args:
        chosen = []
        for i in range(0, 10):
            choice = countryList[random.randint(0, len(countryList)-1)]
            truth = True
            while truth:
                if(choice[0:len(choice)-1] in chosen) or (choice[0:len(choice)-1] in allchosen):
                    choice = countryList[random.randint(0, len(countryList)-1)]
                else:
                    truth = False
                    chosen.append(choice[0:len(choice)-1])
                    allchosen.append(choice[0:len(choice)-1])
        listArr.append(chosen)
    return listArr
