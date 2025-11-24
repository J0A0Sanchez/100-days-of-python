"""Recreate this program: https://appbrewery.github.io/python-day9-demo/"""

import os
name_bid_dict = {}

other_bidders = "yes"

while other_bidders == "yes":
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))
    name_bid_dict[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes or 'no':")
    os.system("cls")


# max_name = max(name_bid_dict, key=name_bid_dict.get)
# max_bid = name_bid_dict[max_name]

# print(f"The winner is {max_name} with a bid of ${max_bid}")


max_bid = 0
max_name = ""

for name in name_bid_dict:
    bid = name_bid_dict[name]
    if bid > max_bid:
        max_bid = bid
        max_name = name

print(f"The winner is {max_name} with a bid of ${max_bid}")