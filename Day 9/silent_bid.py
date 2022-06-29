from art import logo
from os import system

print(logo)

print("Welcome to the secret auction program.")

bidding = True
bidders = {}

def highest_bidder():
    winner = ""
    max_bid = 0
    for name in bidders:
        if bidders[name] > max_bid:
            max_bid = bidders[name]
            winner = name
    print(f"The winner is {winner} with a bid of ${max_bid}.")

while bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid

    keep_bidding = input("Are there more bidders? Type 'yes' or 'no'")
    if keep_bidding == "no":
        system("clear")
        bidding = False
        highest_bidder()
    elif keep_bidding == "yes":
        system("clear")

