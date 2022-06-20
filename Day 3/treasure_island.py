print('''
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
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("You have just landed on Treausre Island, but have lost your map. In the sand in front of you two arrows made out of coconuts is laid out pointing LEFT or RIGHT.")
turn = input("Which direction do you choose? ").lower()

if turn == "left":
  print("You turned left and came to a rushing river. You can either SWIM across or WAIT until the river calms.")
  swim = input("Which do you choose? ").lower()
  if swim == "wait":
    print("The river eventually calmed down and you were able to safely cross. On the other side, you to a wall with 3 doors colored RED, BLUE, and YELLOW.")
    door = input("Which door do you open?").lower()
    if door == "yellow":
      print("Congratulations! You have found the treasure!")
    elif door == "red":
      print("You walked through the red door into a pit of fire. Game Over.")
    else:
      print("You walked into a room of cannibals. Game Over.")
  else:
    print("You tried to swim but were swept back out to sea. Game Over.")
else:
  print("You fell into a snake pit. Game Over!")

  