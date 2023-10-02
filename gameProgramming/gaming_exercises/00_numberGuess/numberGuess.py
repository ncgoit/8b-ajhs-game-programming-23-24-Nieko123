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
# IMMEDIATE CRASH WHEN RUNNING CODE, INDICATES NO TESTING WAS DONE. 
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
# Print(secretNumber)

# GAME LOOP
print("You need to guess a number from 0 to 20 and you have four guesses. \nIf you get guess it right you get a point.\nIf you can't guess it right the cpu gets a point")
# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND.
# print() an explanations of your three difficulty levels.
# Use input() to store difficulty in difficulty variable.
# assign values to numAttempts, rangeMin, and rangeMax based on choice.

while playerScore != 3 and cpuScore != 3: # CHANGE TO and 
    #pass -- Tells Python to skip this block of code.
    #Difficulty code needs to be BEFORE the round starts

    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    #Print(secretNumber)
    # ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND.
    #Difficulty levels go 1-3
    # YOU NEED TO EXPLAIN WHAT THE DIFFICULTY LEVELS ARE! 
    difficulty = input("what difficulty would you like to select?")
    if difficulty == "Easy":
        print("This is easy mode you have 2 guesses to guess a number 1-3")
        numbGuesses = 2
        rangeMin = 1
        rangeMax = 3
    elif difficulty == "Meduim":
        print("This is meduim mode you have 5 guesses for numbers 1-15")
        numbGuesses = 5
        rangeMin = 1
        rangeMax = 15
    elif difficulty == "Hard":
        print("This is hard mode be ready you have 4 guesses 1-25")
        numbGuesses = 4
        rangeMin = 1
        rangeMax = 25
    else:
        print("Not the right answer, We are setting it to easy")
        numbGuesses = 2
        rangeMin = 1
        rangeMax = 3
    secretNumber = random.randint(rangeMin, rangeMax)


    numAttempts = 0
    for guesses in range(4): # Use numGuesses instead of 4.  
        numGuesses = 0
        print(f"You have {4 - numGuesses} guesses remaining.\n") # Use numAttempts instead of 4.  
        playerGuess = int(input(f"Type a number from {rangeMin} to {rangeMax} and press ENTER.\n"))
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
        numAttempts += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses.\n")

if playerScore >= 3:
        print("Winner, winner, chicken dinner! You scored 3 points first.\n")
else:
        print("Yo, you lost to a computer. Youare a scrub.\n")
          
 