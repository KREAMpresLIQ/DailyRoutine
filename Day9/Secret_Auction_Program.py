from Art import logo
import sys, subprocess

# pythontutor.com

print(logo)

bids = {}
bidding_finished = False


def clear_screen():
    operating_system = sys.platform

    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    elif operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear', shell=True)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # {"John": 123, "Elliot":321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your Bid?: $"))
    bids[name] = price
    should_continue = input("Are they any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear_screen()
