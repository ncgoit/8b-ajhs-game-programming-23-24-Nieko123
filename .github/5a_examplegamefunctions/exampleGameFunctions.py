# Example Game Function project, Nieko Garnes v0.0
import random

def startRace():
    pass

def raceDistance(param1):
    pass

def hurdleSuccess(param1 = "Default Value"):
    pass

def raceOutcome(param1, param2, param3):
    pass

def raceOutcome(laps, speed, place):
    if laps > 1 and speed >= 50 and place == 'Won':
        raceOutcome = True
    elif laps > 1 and speed >= 50 and place == 'lose':
        raceOutcome = False
    else:
        print(' Aww man, You lose!\n')
        raceLose = True
        return raceLose
    return raceOutcome



