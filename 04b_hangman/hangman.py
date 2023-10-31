#Nieko Garnes 8b hangman v0.0

words = 'glizzy, star, door, list, man, hang, spring, shorts, king, queen, prince, sobber, drunk, kill, taco, burger, chicken, fries, car, bus, code, zebra, lion, grass, feild,young, yellow, red, purple, word'.split()

#VARIABLE_NAMES IN ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
      0    l
     /l\   l
     / \   l
    =======''','''
    +---+
      0    l
     /l\   l
     / \   l
    =======''','''
    +---+
      0    l
     /l\   l
     / \   l
    =======''','''
    +---+
      0    l
     /l\   l
     / \   l
    =======''','''
    +---+
      0    l
     /l\   l
     / \   l
    =======''','''
    +---+
      0    l
     /l\   l
     / \   l
    =======''','''
    +---+
      0    l
     /l\   l
     / \   l
    =======''']

i = 0
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i += 1


