'''
    File name: PlayoffTeamGenerator.py
    Author: Peter
    Date created: 13.06.2018
    Date last modified: 13.06.2018
    Python Version: 2.7
'''

import random
import datetime

import os
import time 
import sys 

from random import randint
clear = lambda: os.system('cls')

NUMBER_OF_TEAMS =  8
NUMBER_OF_PLAYERS_PER_TEAM = 2


playerList = ["Volkmar", "Peter", "Thomas", "Preity", "Dirk", "Franny", "Jana", "Dennis", "Julian", "Tobi", "Alex", "Jonas", "Leon", "Soeren"]
teamNames = ["Kubba Libre", "KUBBernauten", "Kubbteam schwedisches Bettenlager", "Kibb Kabb Kubb", "KUBBhunters", "Die 3 Kubbketiere", "Kubb'Ings", "Drei Engel fuer Kubb", "Lord of the Kubbs", 
              "Penaltykubber", "Kubbinator", "City-KUBBaner", "Alles fuer den Dackel, alles fuer den Kubb", "Schwubb-die-Kubb", "Supreme de la Kubb", "kubbik^3", "Kubbtrahenden", "Chaoskubber", 
              "Konkubbinen", "Kubb mal da", "Kubbteam Schwedisches Bettenlager"]
teamList = []

 

def getRandomValue(number_of_players_left):
    return (randint(0,number_of_players_left-1))


class kubbPlayer(object):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name 
        
class kubbTeam(object):
    def __init__(self, name):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        if(player):
            if(self.numberOfPlayers() < NUMBER_OF_PLAYERS_PER_TEAM):
                self.players.append(player)
                return True            
        return False

    def numberOfPlayers(self):
        return len(self.players)

    def __repr__(self):
        retVal =  "Teamname: " + self.name + ", "
        
        if (len(self.players)):
            retVal = retVal + "Members: " + str(self.players)
        else:
            retVal = retVal + "Members: -"
        return retVal
     
            
def checkPlayerlist():
    counter = 0
    for x in range (0, NUMBER_OF_PLAYERS_PER_TEAM * NUMBER_OF_TEAMS - len(playerList)):
        counter += 1
        playerList.append("-")        
    print "added players:" + str(counter) 

def createTeams():    
    print "Teamnamen: "
    for x in range(0, NUMBER_OF_TEAMS): 
        
        tempTeamName = teamNames[getRandomValue(len(teamNames))]
        print "\t"+tempTeamName 
        teamList.append(kubbTeam(tempTeamName))
        teamNames.remove(tempTeamName)

def load(left_side, right_side, length, timeout):
    # based upon https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    x = 0
    y = ""
    print "\r"
    while x < length:
        space = length - len(y)
        space = " " * space
        z = "Shuffle Players - " + left_side + y + space + right_side
        print "\r", z,
        y += "#"
        time.sleep(timeout)
        x += 1
    clear()
    printHeader()

def createPlayoffPicture():
    number_of_players = len(playerList)
    for x in range(0, number_of_players):
        pos = getRandomValue(len(playerList)) 
        player =  kubbPlayer(playerList[pos])

        for team in teamList:
            if (team.addPlayer(player)):
                break
        
        playerList.remove(playerList[pos]) 
        random.shuffle(playerList) 
        load("|", "|", 10, .01)
        print ""
        for team in teamList:
            print team  

def createGameplan():
    print "\n\rSpielplan:"
    teamValues = range(0, len(teamList))
     
    for x in range(0, NUMBER_OF_TEAMS/2):
        pos = random.choice(teamValues)
        team1 = teamList[pos]
        teamValues.remove(pos)
        pos = random.choice(teamValues)
        team2 = teamList[pos]
        teamValues.remove(pos)

        print team1.name + " vs. " + team2.name
        print team1.players," vs. ",team2.players
        print ""

def printHeader():
    print "Kubb-Weltmeisterschafts-Playoff Generator " + str(now.year)
    print "Anzahl Teams: " + str(NUMBER_OF_TEAMS)
    print "Anzahl Spieler / Team: " + str(NUMBER_OF_PLAYERS_PER_TEAM)

if __name__ == '__main__': 
    now = datetime.datetime.now()
    checkPlayerlist()
    createTeams()
    createPlayoffPicture()
    clear()
    printHeader()
    print ""

    for team in teamList:
        print team 

    createGameplan()

    print "Happy KUBBing"
