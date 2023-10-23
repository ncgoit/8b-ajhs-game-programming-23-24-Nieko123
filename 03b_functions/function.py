# Function -- a named piece of code that can be rueses easily.
# FUNCTION SIGNATURE -- Syntax for creating a new function
def exampleFunctionA():
    count = 0
    num = int(input("how many times do you want to wish a happy birthday?\n"))
    while count < num:
        print("Happy Birthday!\n")
        count += 1
    
def exampleFunctionB(num, count):
    while count < num:
        print("Happy Birthday!\n")
        count += 1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM!

# RUNNING A FUNCTION IS KNOWN AS CALLING THE FUNCTION
exampleFunctionA()
exampleFunctionB(5, 0)


