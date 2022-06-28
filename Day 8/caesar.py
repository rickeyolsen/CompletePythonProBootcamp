from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(old_text, shift_amount):
    new_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in old_text:
        if letter not in alphabet:
            new_text += letter
        else:
            x = alphabet.index(letter)
            y = x + shift_amount
            new_text += alphabet[y]
    print(f"Here's the {direction}d result: {new_text}")

play = True
while play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(old_text=text, shift_amount=shift)

    play_again = input("Type 'yes' if you want to run again. Otherwise type 'no'. ")
    
    if play_again == "no":
        play = False
        print("Goodbye!")