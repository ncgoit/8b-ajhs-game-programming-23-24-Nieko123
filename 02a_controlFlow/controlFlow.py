# Control Flow, Nieko Garnes, v0.3
# DECLARATIONS

favColor = "Blue"
luckyNumber = 7
myGPA = 3.31
myAge = 16
pineappleOnPizza = True

# If Statements - checks for a conditions to be True/False, do something if true.
if favColor == "Blue":
    print("I like your style.")
if luckNumber == 7:
    print("Nice me too")

# if-else Statement -- check for a condition, do something for True and False
if myGPA >= 3.0:
    print("Congrates o making honor Roll")
else:
    print("Better luck next year. Try to study more!")

if myGPA >= 3.0:
    print("Congrates o making honor Roll")
else:
    print("Better luck next year. Try to study more!")


# if - elif - else Statements -- Checks for multiple conditions

if myGPA > 65:
    print("Dang your old")
elif myAge > 50:
    print("Congratulations, you have earned a bonus $1000")
else:
    print("You are not old enough for a bonus.")
# 1 if, else, any number of elif allowed.

# Nested if - elif - else Statements
if myAge > 15:
    print("You are eligible for a license!")
    if myGPA >= 3.5:
        print("You are eligable for a new car")
    elif myGPA > 2.0:
        print("You qualify for $500 off a car!")
    else:
        print("You get nothing!")
else:
    print("You are not old enough to drive")

# When doing if - elif - else statements. check for the highest values first!!!!
if myGPA > 1.5:
    print("You are in danger of failing for the year.")
elif myGPA > 2.0:
    print("You are on track to graduate")
elif myGPA > 3.0:
    print("you can get scholoarship money")
elif myGPA > 3.99:
    print("You qualify for bright futures 100 percent scholarship")
else:
    print("GPA was not calculated. Please try again")

# while Loop -- Think "Musical Chairs" -- Used when you do Not know how many iterations you need.
# Iteraltion = one complete trip through a loop
x = 0
while x < 100: 
    print(f"X is currently equal to {x}")
    x += 1

while x < 0:
    print(f"X is currently equal to {x}")
    x -= 1

# for Loop -- Think 'Go Fish', used when you know nummber of iterationa needed
print("For Loop starts here")
for i in range(10):
    print(i)

print("EVEN OR ODD LOOP!")
for i in range(101):
    print(i)
    if i % 2 == 0:
        print("That number is even!")
    else:
        print("That number is odd!")
        

# () Parentheses
# [] Square Brackets
# <> Angle Brackets
# {} Braces

