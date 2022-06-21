import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Set above options to a list
throw = [rock, paper, scissors]

# Get user choice and convert to integer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Generate random computer choice
comp_choice = random.randint(0,2)

# Check to see if user_choice is within range and if so print throw options
if user_choice >= 0 and user_choice < 3:
  print(throw[user_choice])
  print(f"Computer chose:\n{throw[comp_choice]}")

# Determine if user wins against computer or give an error if user choice is not within range.
if user_choice < 0 or user_choice >= 3 :
  print("You typed an invalid number, please try again!")
elif user_choice == 0 and comp_choice == 2:
  print("You win!")
elif user_choice == 2 and comp_choice == 0:
  print("You lose.")
elif user_choice > comp_choice:
  print("You win!")
elif user_choice == comp_choice:
  print("Draw! Try again!")
elif user_choice < comp_choice:
  print("You lose!")
