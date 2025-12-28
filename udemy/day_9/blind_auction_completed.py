bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?$ "))

    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False

max_key = max(bids, key=bids.get)
print(f"The winner is {max_key} with a bid of ${bids[max_key]}")

