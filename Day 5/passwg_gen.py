#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_len = nr_letters + nr_symbols + nr_numbers
char = [letters, numbers, symbols]
passwd = []

## Code written without using choice()
# Select random letters and add to passwd list
for x in range(1, nr_letters + 1):
  lett = random.randint(0,51)
  passwd += char[0][lett]

# Select random numbers and add to passwd list
for x in range(1, nr_numbers + 1):
  num = random.randint(0,9)
  passwd += char[1][num]

# Select random symbols and add to passwd list
for x in range(1, nr_symbols + 1):
  sym = random.randint(0,8)
  passwd += char[2][sym]

# Shuffle password 
random.shuffle(passwd)

# Print password to user
print(f"Here is your password: {''.join(passwd)}")
