# Project: Treasure Island
print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input(
    "You're at a T-Junction, where would you like to go? Type 'left' to go left & 'right' to go right \n"
).lower()
if direction == "right":
    print("Gameover, you got hit by a bus")
    quit()
elif direction == "left":
    action = input(
        "You cam across a river, would you swim or wait for a boat? Type 'swim' to swim or 'wait' to wait for a boat \n"
    ).lower()
if action == "swim":
    print("Gameover, you got killed by crocodiles in the river")
    quit()
elif action == "wait":
    print("You're in a room with three doors of different colors. Red, Yellow, Blue")
    door = input("Type 'Red', 'Yellow' or 'Blue' to enter the corresponding door \n").lower()
if door == "red":
    print("Gameover, Red door leads to a black hole")
    quit()
elif door == "blue":
    print("Gameover, Blue door leads to a black hole")
    quit()
elif door == "yellow":
    print('''

                                 _       
                                | |      
            ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
            / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
            | (_| (_) | | | | (_| | | | (_| | |_\__ \
            \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                            __/ |                  
                            |___/                   

        ''')
    print("You found the treasure")
