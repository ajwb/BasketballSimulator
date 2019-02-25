#DRAFT LOTTERY SIMULATOR by ALEX BROWN
#This is my little NBA draft lottery simulator. It runs a simulation
#of a season and then based on the position a team placed they enter the draft
#lottery in order to try to draft players that are better than their current
#lineup. There are just 5 players per team, each with a skill level between 60
#and 99, 99 being the best player (very rare).

### THINGS TO DO ###
# DONE******get classes functional: TEAM, PLAYER, ...
# DONE******allow teams to play against eachother, taking into account skill of players
# DONE******create season with list of rankings
# DONE******ai for draft, take into account position, skill, etc.
# DONE******create draft class each season
# DONE******add draft lottery
# make a human controlled team
# add name database and team name database
# redo the way games are played in a season
# make it so teams can't tie


import random
skillDist = [87, 93, 75, 80, 94, 75, 80, 76, 89, 81, 88, 76, 87, 81, 92, 78, 74,
             88, 69, 83, 67, 87, 71, 97, 92, 68, 89, 82, 84, 84, 83, 69, 84, 70,
             71, 79, 79, 74, 87, 84, 89, 65, 94, 86, 73, 78, 72, 89, 82, 74, 80,
             83, 95, 83, 78, 61, 74, 89, 69, 63, 85, 65, 88, 75, 71, 68, 82, 69,
             78, 73, 66, 67, 65, 60, 82, 72, 89, 77, 95, 62, 88, 75, 70, 71, 77,
             73, 65, 72, 85, 70, 81, 78, 88, 75, 89, 72, 78, 90, 86, 69, 66, 76,
             86, 80, 70, 66, 71, 69, 93, 83, 68, 72, 82, 63, 83, 94, 76, 76, 78,
             84, 84, 87, 73, 89, 88, 87, 74, 67, 84, 92, 71, 92, 73, 71, 80, 88,
             85, 81, 78, 90, 66, 86, 82, 87, 96, 63, 69, 68, 80, 74, 98, 99]
PositionChoice = ["PG", "SG", "SF", "PF", "C"]
NameChoice = ["Bob", "John", "Joe", "Lebron", "Mike", "Reggie", "Jordan", "Alex",
              "Sam", "Jack", "Keeyan", "Jake", "Ron", "Max", "Christian", "Manuel",
              "Jerome", "Axel", "Justin", "Marko", "Roberto", "Kostas", "Danny",
              "Thomas", "Courtney", "Court", "Andy", "Paul", "Dave", "Quinton", "Levi",
              "Josh", "Jacob", "Trevor"]
TeamNameChoice = ["Falcons", "Lions", "Fire", "Turtles", "Geese", "Dinos",
                  "Friends", "Tigers", "Tarantulas", "Zippers", "Trees",
                  "Kitties", "Puppies", "Lads", "M&Ms", "Schwarmas", "Ploppers",
                  "Cowguys", "Big Boys", "Weiners", "Terrors",
                  "Cleaners"]

class Team: #CLASS for each team
    def __init__(self, name, players):
        self.name = name
        self.players = players #list of players, declared on init
        self.wins = 0
        self.losses = 0
        self.rawdraft = 0 #unchanged draft odds number
        self.draftodds = 0 #altered draft odds number (explained in CreateOdds fxn)
        self.gamesplayed = 0
        self.skillaverage = 0
        self.championships = 0

class Player: #Class for each player
    def __init__(self, name, skill, position):
        self.name = name
        self.skill = skill
        self.position = position

def sortRank(ranking): #Simple sort to sort rankings, at most 16 teams
    for i in range(1,len(ranking)):
        currentvalue = ranking[i]
        position = i

        while position>0 and ranking[position-1].wins<currentvalue.wins:
            ranking[position]=ranking[position-1]
            position = position-1

        ranking[position]=currentvalue
    return ranking

def sortDraftClass(draftClass):
    for i in range(1,len(draftClass)):
        currentvalue = draftClass[i]
        position = i

        while position > 0 and draftClass[position-1].skill < currentvalue.skill:
            draftClass[position] = draftClass[position-1]
            position = position-1

        draftClass[position] = currentvalue
    return draftClass

def game(hometeam, awayteam):
    homeskill = 0
    awayskill = 0
    for i in range(5):
        homeskill = homeskill + hometeam.players[i].skill
        awayskill = awayskill + awayteam.players[i].skill

    totalskill = homeskill + awayskill

    firstcheckwinner = random.randint(0, totalskill)
    hometeamadv = random.randint(1, 5)

    if firstcheckwinner >= 0 and firstcheckwinner <= homeskill:
        winner = hometeam
    elif firstcheckwinner > homeskill and firstcheckwinner <= totalskill:
        winner = awayteam

    if winner == awayteam:
        if hometeamadv == 5:
            winner = hometeam

    return winner

def season(teams):
    numTeams = len(teams)

    for i in range(numTeams):

        for j in range(i+1, numTeams):

            print("Now playing:", teams[i].name, "vs", teams[j].name)
            gameOneWinner = game(teams[i],teams[j])
            if gameOneWinner == teams[i]:
                teams[i].wins += 1
                teams[j].losses += 1
                print(teams[i].name, "won game 1!")
            else:
                teams[j].wins += 1
                teams[i].losses += 1
                print(teams[j].name, "won game 1!")

            gameTwoWinner = game(teams[j],teams[i])
            if gameTwoWinner == teams[i]:
                teams[i].wins += 1
                teams[j].losses += 1
                print(teams[i].name, "won game 2!")

            else:
                teams[j].wins += 1
                teams[i].losses += 1
                print(teams[j].name, "won game 2!")
            teams[i].gamesplayed += 2
            teams[j].gamesplayed += 2
            print("Press ENTER to continue...")
            input()
    print("The season is over!")
    teams = sortRank(teams)

##    maxwins = teams[0].wins
##    tieteams = [teams[0]]
##    for i in range(1,len(teams)-1):
##        if teams[i].wins == maxwins:
##            tieteams.append(teams[i])
##    if len(tieteams) != 1:
##        print("There was a", len(tieteams),"way tie for first!")
##        print("We will now enter a tiebreaker phase to find a winner!")
##        print("Here are the teams participating:")
##        for i in range(len(tieteams)):
##            print(tieteams[i].name)

    print("The winner is...")
    print("Press ENTER to continue...")
    input()
    print("The",teams[0].name, "with", teams[0].wins, "wins!\n")
    teams[0].championships += 1
    print("Here is the final table")
    for i in range(numTeams):
        print(i+1,":",teams[i].name, "->", teams[i].wins, "wins")
    print("\n")
    return teams

def ranSkill():
    skillVal = random.choice(skillDist)
    return skillVal

def ranName():
    name = random.choice(NameChoice)
    return name

def ranPos():
    random.seed()
    position = random.choice(PositionChoice)
    return position

def ranTeamName():
    name = random.choice(TeamNameChoice)
    return name

def CreatePlayer(team, posChoice, pos):
    name = ranName()
    skill = ranSkill()
    if (posChoice == False):
        position = pos
    else:
        position = ranPos()
    player = Player(name, skill, position)
    return player


def CreateTeams(numTeams):
    Teams = []
    names = []
    for i in range(numTeams):
        flag = 0
        while flag == 0:
            name = ranTeamName()
            if name not in names:
                names.append(name)
                flag = 1

        players = []
        players.append(CreatePlayer(name, False, "PG"))
        players.append(CreatePlayer(name, False, "SG"))
        players.append(CreatePlayer(name, False, "SF"))
        players.append(CreatePlayer(name, False, "PF"))
        players.append(CreatePlayer(name, False, "C"))
        team = Team(name, players)
        team.skillaverage = getSkillAverage(team)
        Teams.append(team)
    return Teams

def getSkillAverage(team):
    totalskill = 0
    for i in range(5):
        totalskill += team.players[i].skill
    totalskill = totalskill/5
    return totalskill

def PrintTeams(Teams):
    for i in range(len(Teams)):
        Teams[i].skillaverage = getSkillAverage(Teams[i])
        print (i+1, Teams[i].name, "-------------", int(Teams[i].skillaverage), "Overall")
        print ("PG", Teams[i].players[0].name, "->", Teams[i].players[0].skill)
        print ("SG", Teams[i].players[1].name, "->", Teams[i].players[1].skill)
        print ("SF", Teams[i].players[2].name, "->", Teams[i].players[2].skill)
        print ("PF", Teams[i].players[3].name, "->", Teams[i].players[3].skill)
        print ("C", Teams[i].players[4].name, "->", Teams[i].players[4].skill)
        print ("-------------------", Teams[i].championships, "league wins")
        print ("\n")

def ResetStats(Teams):
    for i in range(len(Teams)):
        Teams[i].wins = 0
        Teams[i].losses = 0

def CreateDraftClass(numClass):
    draftClass = []
    dictClass = {}
    for i in range(numClass):
        draftClass.append(CreatePlayer(ranName(),True, "Nothing"))
    draftClass = sortDraftClass(draftClass)
    PrintDraftClass(draftClass, numClass)
    draftClassPG = draftClass
    draftClassSG = draftClass
    draftClassSF = draftClass
    draftClassPF = draftClass
    draftClassC = draftClass
    dictClass[0] = SeparateDraftClassPos(draftClassPG, "PG")
    dictClass[1] = SeparateDraftClassPos(draftClassSG, "SG")
    dictClass[2] = SeparateDraftClassPos(draftClassSF, "SF")
    dictClass[3] = SeparateDraftClassPos(draftClassPF, "PF")
    dictClass[4] = SeparateDraftClassPos(draftClassC, "C")

    return dictClass

def PrintDraftClass(draftClass, numClass):
    print("The new draft class:")
    for i in range(numClass):
        print(i+1, draftClass[i].name, "->", draftClass[i].skill, "->", draftClass[i].position)
    print("\n")

def SeparateDraftClassPos(draftClass, pos):
    posClassSize = len(draftClass)
    posClass = []
    i = 0
    while i < posClassSize:
        if draftClass[i].position == pos:
            posClass.append(draftClass[i])
        i += 1
    return posClass

def SelectDraftPlayer(team, dictClass):
    maxGain = 0
    skillGain = 0
    for i in range(5):
        if len(dictClass[i]) != 0:
            skillGain = dictClass[i][0].skill - team.players[i].skill
        if skillGain > maxGain:
            maxGain = skillGain
            choosePlayer = dictClass[i][0]
            positionindex = i
    if maxGain == 0:
        print("The", team.name, "decide to forego their pick in the draft")
        input("press ENTER to continue...\n")
        return dictClass
    else:
        playerPos = choosePlayer.position
        team.players[positionindex] = choosePlayer
        print("The", team.name, "choose", choosePlayer.name, "->", choosePlayer.skill, "->", choosePlayer.position)
        input("press ENTER to continue...\n")
        dictClass = DeleteDraftedPlayer(dictClass, positionindex)
        return dictClass

def DeleteDraftedPlayer(dictClass, playerPosNumber):
    listDelete = dictClass.pop(playerPosNumber)
    del listDelete[0]
    dictClass[playerPosNumber] = listDelete
    return dictClass

def OrderDraw(lefttodraft,total,draftOrder,pick):
    numLeft = len(lefttodraft)
    current = 0

    if numLeft == 1:
        draftOrder.append(lefttodraft[0])
        print("The final pick for the draft goes to the...")
        input("Press ENTER to continue...\n")
        print(lefttodraft[0].name,"\n")
        return draftOrder

    elif numLeft > 1:
        for i in range(numLeft):
            lefttodraft[i].draftodds += current
            current += lefttodraft[i].rawdraft

        draw = random.randint(0, total)
        flag = 0
        i = 0
        while flag == 0:
            if draw <= lefttodraft[i].draftodds:
                flag = 1
                total = total - lefttodraft[i].rawdraft
                draftOrder.append(lefttodraft[i])
            else:
                i += 1

        print("The number",pick,"pick for the draft goes to the...")
        input("Press ENTER to continue...\n")
        print(lefttodraft[i].name,"\n")
        pick += 1
        del lefttodraft[i]
        newlength = len(lefttodraft)
        for i in range(newlength):
            lefttodraft[i].draftodds = lefttodraft[i].rawdraft

        draftOrder = OrderDraw(lefttodraft,total,draftOrder,pick)
    return draftOrder

def CreateDraftOrder(teamsList):
    draftOrder = []
    lefttodraft = teamsList
    numTeams = len(teamsList)
    total = 0
    for i in range(numTeams):
        chance = int(((teamsList[i].losses)/(teamsList[i].gamesplayed*2))*1000)
        teamsList[i].rawdraft = chance
        teamsList[i].draftodds = chance
        total += teamsList[i].rawdraft

    pick = 1
    draftOrder = OrderDraw(lefttodraft,total,draftOrder,pick)
    return draftOrder

def PrintDraftOrder(draftOrder):
    length = len(draftOrder)
    print("The final order for the draft is:")
    input("Press ENTER to continue...")
    for i in range(length):
        print(i+1, draftOrder[i].name)
    print("\n")

def Draft(teams):
    numClass = len(teams) * 2
    dictClass = CreateDraftClass(numClass)
    draftOrder = CreateDraftOrder(teams)
    PrintDraftOrder(draftOrder)
    for i in range(len(draftOrder)):
        dictClass = SelectDraftPlayer(draftOrder[i], dictClass)

    return draftOrder

def main():
    exitGame = False
    seasonNumber = 1

    print("Welcome to NBA Draft Simulator by Alex Brown")
    print("Currently the draft feature is not implemented so it's more of a NBA season simulator")
    print("Let's get started!")
    checkinput = 0
    while(checkinput == 0):
        print("How many teams should be in the league? CHOOSE 4,8,12,16")
        numTeams = input("Enter a value here: ")
        if numTeams == "4" or numTeams == "8" or numTeams == "12" or numTeams == "16":
            checkinput = 1
    print("\nHere are the teams and players:")
    Teams = CreateTeams(int(numTeams))
    PrintTeams(Teams)
    print("Press ENTER to continue...")
    input()
    print("Each season consists of the teams playing each other twice")
    print("Press ENTER to begin season 1...")
    input()
    while(exitGame == False):
        ResetStats(Teams)
        if (seasonNumber != 1):
            print("Press ENTER to begin season", seasonNumber, "...")
            input()
        Teams = season(Teams)
        print("It's time for the post-season draft")
        input("Press ENTER to continue...\n")
        Teams = Draft(Teams)
        print("Here are the updated teams after the draft")
        PrintTeams(Teams)
        print("Would you like to play another season?")
        againResponse = input("Y for yes, N for no: ")
        if againResponse == "N" or againResponse == "n":
            exitGame = True
            print("Okay! Thanks for playing!")
            exit()
        seasonNumber += 1

main()
