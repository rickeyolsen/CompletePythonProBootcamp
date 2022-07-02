import random
from os import system
from art import logo

# Set variables for game
user_cards = []
dealer_cards = []
user_score = 0
dealer_score = 0
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def new_card():
    x = random.randint(0, len(cards))
    return x

def sum(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total

def add_user_card():
    x = random.randint(0, len(cards))
    user_cards.append(cards[x])

def check_score():
    if user_score == dealer_score:
        print("Draw!")
    elif user_score == 21:
        print("You win!")
    elif user_score > dealer_score and user_score < 21:
        print("You win!")
    elif dealer_score > 21 and user_score < 21:
            print("You win!")
    else:
        print("You lose.")

def blackjack():
    print(logo)
    global user_score 
    global dealer_score
    global user_cards
    global dealer_cards

    # Deal cards
    for i in range(4):
        if i == 0 or i == 2:
            user_cards.append(cards[new_card()])
        else:
            dealer_cards.append(cards[new_card()])

    play = True
    while play:
        user_score = sum(user_cards)
        print(f"Your cards: {user_cards}, your score: {user_score}")
        print(f"The first dealer card is: {dealer_cards[0]}")

        if user_score > 21:
            dealer_score = sum(dealer_cards)
            print(f"Your final hand is: {user_cards}, your final score: {user_score}")
            print(f"The dealer's final hand is: {dealer_cards}, final dealer score: {dealer_score}")
            print("You went over. You lose.")
            break
        elif user_score == 21:
            while dealer_score < 17:
                dealer_cards.append(cards[new_card()])
                dealer_score = sum(dealer_cards)
            print(f"Your final hand is: {user_cards}, your final score: {user_score}")
            print(f"The dealer's final hand is: {dealer_cards}, final dealer score: {dealer_score}")
            play = False
            check_score()
        else:
            keep_playing = input("Type 'y' to get another card, type 'n' to stand: ")

            if keep_playing == 'n':
                play = False
                dealer_score = sum(dealer_cards)
                while dealer_score < 17:
                    dealer_cards.append(cards[new_card()])
                    dealer_score = sum(dealer_cards)
                print(f"Your final hand is: {user_cards}, your final score: {user_score}")
                print(f"The dealer's final hand is: {dealer_cards}, final dealer score: {dealer_score}")
                check_score()
                break
            else:
                add_user_card()

    play_again= input("Do you want to play again? Type 'y' or 'n': ")

    if play_again == "y":
        system("clear")
        user_cards = []
        dealer_cards = []
        user_score = 0
        dealer_score = 0
        blackjack()

# Prompt user to initiate a game of blackjack
initiate_game = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

# If user chose 'y', run blackjack game. End if not.
if initiate_game == "y":
    system("clear")
    blackjack()
else:
    print("Maybe next time!")