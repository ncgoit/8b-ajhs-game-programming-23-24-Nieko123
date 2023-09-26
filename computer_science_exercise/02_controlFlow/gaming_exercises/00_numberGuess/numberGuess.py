# Select the secret number from a given range.
# Players must guess the number
# Compare guess to the secret number.
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    # Tell thwe the number of guesses left.
    # Tell them if too high / too low.
# What happens if the guess is right?
    # Tell them guess is correct
    # Award a point
# What happens if the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU.
# Check to see if player or CPU has >= 3 points, if so they win.

import random # Import the random module to our code.

# Declarations
secretNumber = -1
playerGuess = -1 
playerScore = 0
cpuScore = 0
numGuesses = 0
playName = ""
difficulty = ""
rangeMin = -1
rangeMax = -1
numAttempts = -1

print("""
    *~~~~~~~~~~~~~~~~~~~~~~~*
    |                       |
    |     Guess The number  |
    |       Nieko Garnes     |
    |           2023        |
    *~~~~~~~~~~~~~~~~~~~~~~~*
    """)

# CPU SECRET NUMBER GENERATION
    secretNumber = random.randint(0, 20)

# GAME LOOP
print("You need to guess a number from 0 to 20 and you have four guesses. \nIf you get guess it right you get a point.\nIf you can't guess it right the cpu gets a point")
# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND.
# print() an explanations of your three difficulty levels.
# Use input() to store difficulty in difficulty variable.
# assign values to numAttempts, rangeMin, and rangeMax based on choice.

while playerScore != 3 or cpuScore != 3:
    #pass -- Tells Python to skip this block of code.
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    secretNumber = random.randint(rangeMin, rangeMax)
    #Print(secretNumber)
    # ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND.

    
    for guesses in range(4):
        numGuesses = 0
        print(f"You have {4 - numGuesses} guesses remaining.\n")
        playerGuess = int(input("Type a number from 0 - 20 and press ENTER.\n"))
        # input() saves all data as a STRING by defualt.
        # int() will convert to an INTERGER
        # float() will convert to a FLOAT
        print(f"You have chosen {playerGuess}. Lets see if you're right!\n")
        if playerGuess == secretNumber: 
            print("Whoa dude, what a guess! You got it!\n")
            playerScore += 1
            break # IMMEDIATELY EXIST ANY LOOP YOU ARE IN!
        else:
            print("You did not guess correctly.\n")
            if playerGuess > secretNumber:
                print("Your guess is too high.\n")
            else:
                print("Your guess is too low.\n")
        numGuesses += 1
    if playersGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses.\n")
    if playerScore >= 3:
        print("Winner, winner, chicken dinner! You scored 3 points first.\n")
    else:
        print("Yo, you lost to a computer. Youare a scrub.\n")

if playerScore >= 3:
    print("Winner, winner, chicken dinner! you scored 3 points first!\n")
else:
    print("Yo, you lost, lol\n")    
 