#Nieko Garnes 8b hangman v0.0
import random
words = 'glizzy, star, door, list, man, hang, spring, shorts, king, queen, prince, sobber, drunk, kill, taco, burger, chicken, fries, car, bus, code, zebra, lion, grass, feild,young, yellow, red, purple, word'.split()

#VARIABLE_NAMES IN ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
           l
           l
           l
    =======''','''
    +---+
      0    l
           l
           l
    =======''','''
    +---+
      0    l
      l    l
           l
    =======''','''
    +---+
      0    l
     /l    l
           l
    =======''','''
    +---+
      0    l
     /l\   l
           l
    =======''','''
    +---+
      0    l
     /l\   l
     /     l
    =======''','''
    +---+
      0    l
     /l\   l
     / \   l
    =======''']

# Pick Word from List
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordList) - 1)
    # len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordList[wordIndex]

def displayBoard(,missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()
   
    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
        print()

        blanks = '_' * len(secretWord)

        # Replace Blanks with Correct Letters
        for i in range(len(secretWord)):
            if secretWord[i] in correctLetters:
                blanks =  blanks[:i] + secretWord[i] + blanks[i+1:]

        for letter in blanks:
            print(letter, end = '')
          print()

# i = 0
# while i < 100:
#     word = getRandomWord(words)
#     print(word)
#     i += 1


