from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

stop_bid = False
bids = {}

while stop_bid != True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))

    bids[name] = bid
    
    while True:
        more_bids = input("Are there any other bidders (yes/no)?: ")
        if more_bids == "yes":
            os.system("clear")
            break
        elif more_bids == "no":
            stop_bid = True
            break
        else:
            print("Invalid Input. Type (yes or no)")
            continue

# print(bids)
winner_bid = max(bids.values())
winner = None
for key in bids:
    if bids[key] == winner_bid:
        winner = key
        break
print(f"The winner is {winner} with a bid of ${winner_bid}")