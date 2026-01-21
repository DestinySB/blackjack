import random

# Populates deck with a standard 52 card deck based on ranks.
def load_deck():
    deck = []
    # Loading the deck with 4x each rank (1-13, 11 = J, 12 = Q, 13 = K)
    for suit in range(0, 4):
        for rank in range(1, 14):
            deck.append(rank)
    random.shuffle(deck)
    return deck

def blackjack():
    deck = []
    player = 0
    dealer = 0

    deck = load_deck()

    player += deck.pop()
    dealer += deck.pop()
    player += deck.pop()
    dealer += deck.pop()

    choice =  ""

    # Player phase
    while (choice != "s"):
        print("Player hand: " + str(player))
        print("Dealer hand: " + str(dealer))
        print("")
        choice = input("To hit, enter \"h\". To stand, enter \"s\": ")

        if (choice == "h"):
            player += deck.pop()
            continue
        elif (choice == "s"):
            break
        else:
            print("Enter only either 'h' or 's'.")
            continue

    if player > dealer:
        print("You win!")
    elif dealer > player:
        print("Dealer wins.")
    else:
        print("It's a draw.")

blackjack()
