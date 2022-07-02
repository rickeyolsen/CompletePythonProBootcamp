import random
from os import system
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
dealer_cards = []
user_score = 0
dealer_score = 0

def sum(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total

def add_user_card():
    x = random.randint(0, len(cards))
    user_cards.append(cards[x])
    print(f"Your cards: {user_cards}, your score: {user_score}")
    print(f"The first dealer card is: {dealer_cards[0]}")

# def add_dealer_card():

def blackjack():
    print(logo)

    # Deal cards
    for i in range(4):
        x = random.randint(0, len(cards))
        if i == 0 or i == 2:
            user_cards.append(cards[x])
        else:
            dealer_cards.append(cards[x])

    play = True
    while play:
        user_score = sum(user_cards)
        print(f"Your cards: {user_cards}, your score: {user_score}")
        print(f"The first dealer card is: {dealer_cards[0]}")
        keep_playing = input("Type 'y' to get another card, type 'n' to stand: ")
        if user_score > 21:
            print(f"Your final hand is: {user_cards}, your final score: {user_score}")
            print(f"The dealer's final hand is: {dealer_cards}, final dealer score: {dealer_score}")
            print("You went over. You lose.")
        if keep_playing == 'n':
            play = False
            dealer_score = sum(dealer_cards)
            print(f"Your final hand is: {user_cards}, your final score: {user_score}")
            print(f"The dealer's final hand is: {dealer_cards}, final dealer score: {dealer_score}")
            if user_score > dealer_score:
                print("You win!")
            elif user_score == dealer_score:
                print("Draw!")
            else:
                print("You lose.")
        else:
            add_user_card()

# Prompt user to initiate a game of blackjack
initiate_game = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

# If user chose 'y', run blackjack game. End if not.
if initiate_game == "y":
    system("clear")
    blackjack()
else:
    print("Maybe next time!")