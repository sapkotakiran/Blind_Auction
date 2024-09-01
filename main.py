def find_highest_bid(bidding_dictionary):
    highest_bid = 0
    winners = []

    for bidder, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winners = [bidder]
        elif bid_amount == highest_bid:
            winners.append(bidder)

    return highest_bid, winners


def auction_program():
    bids = {}
    while True:
        name = input("What is your name? ")
        price = float(input("What is your bid amount?: $"))
        bids[name] = price

        continue_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if continue_bid == "no":
            highest_bid, winners = find_highest_bid(bids)
            if len(winners) > 1:
                print(f"It's a tie between {', '.join(winners)} with a bid of ${highest_bid}.")
                print("Starting another round of bidding for the tied bidders only...\n")

                # New bidding round for tied bidders
                tie_bids = {}
                for winner in winners:
                    price = int(input(f"{winner}, what is your new bid amount?: $"))
                    print("\n" * 100)
                    tie_bids[winner] = price

                highest_bid, final_winner = find_highest_bid(tie_bids)
                if len(final_winner) > 1:
                    print(f"It's still a tie! The winners are {', '.join(final_winner)} with a bid of ${highest_bid}.")
                else:
                    print(f"The winner is {final_winner[0]} with a bid of ${highest_bid}.")
            else:
                print(f"The winner is {winners[0]} with a bid of ${highest_bid}.")
            break
        elif continue_bid == "yes":
            # Clear the console (simulate a screen clear)
            print("\n" * 100)


if __name__ == "__main__":
    auction_program()
