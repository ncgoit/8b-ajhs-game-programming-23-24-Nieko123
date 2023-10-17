# # playerInventory = []

# # while len(playerInventory) < 10: 
# #     item = input("What item do you want to add to the inventory?\n")
# #     playerInventory.append(item)

# # playerInventory.sort()
# # print(playerInventory)

# # while len(playerInventory) > 5:
# #     input("What item do you want to add to the inventory?\n")
# #     playerInventory.remove(item)

# # playerInventory.sort()
# # print(playerInventory)

# doorKeys = [
#     "red",
#     "green",
#     "yellow",
#     "purple",
#     "browns"
# ]

# keys = input("which color key doyou need to unlock the door?\n")

# if key in doorKeys:
#     print("You have the correct key! The door unlocks.\n")
# else:
#     print("You do not have that key. The door remain locked\n")

weaponList = [
    True, # sword
    False, # laser blaster
    False, # flame thrower
    False, # gun that shoots more guns
    True, # grappling hook
    False, # missile launcher
    True, # teleporter beam
    True # alien blaster
]

weaponNum = 0
while weaponNum < len(weaponList):
    if weaponNum == 0 and weaponList[0] == True:
        print("You are wielding a shiny sword.\n")
    if weaponNum == 0 and weaponList[1] == True:
        print("You have a toasty flamethrower.\n")
    if weaponNum == 0 and weaponList[2] == True:
        print("You got a gun that shoots more guns.\n")
    if weaponNum == 0 and weaponList[3] == True:
        print("You have a grappling hook.\n")
    if weaponNum == 0 and weaponList[4] == True:
        print("You have a missile launcher.\n")
    if weaponNum == 0 and weaponList[5] == True:
        print("You got a teleporter beam.\n")
    if weaponNum == 0 and weaponList[6] == True:
        print("You are weilding an alien blaster\n")
    weaponNum += 1
    
