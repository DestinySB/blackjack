# Group 2
# Henry Silva
# Cassady Mead
# Lihang Jin
# Destiny Baugh

import random

dealerWin = 0
playerWin = 0
totalDraw = 0

RANKS = [
    "A",
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "J", "Q", "K"
    ]
SUITS = ["c", "d", "h", "s"]

# Populates deck with a standard 52 card deck based on ranks.
def load_deck():
    deck = []
    # Loading the deck with 4x each rank (1-13, 11 = J, 12 = Q, 13 = K)
    for suit in SUITS:
        for rank in RANKS:
            deck.append(f"{rank}")
    random.shuffle(deck)
    return deck

def calculate_hand_value(cards):
    value = 0
    aces_count = 0

    for card in cards:
        if card == "A":
            value += 11
            aces_count += 1
        elif card == "J" or card == "Q" or card == "K":
            value += 10
        else:
            value += int(card)

    # Aces
    while (value > 21 and aces_count > 0):
        value -= 10
        aces_count -= 1

    return value

def blackjack(bet):
    global playerWin, dealerWin, totalDraw

    deck = []
    player = []
    dealer = []

    deck = load_deck()

    player.append(deck.pop())
    dealer.append(deck.pop())

    player.append(deck.pop())
    dealer.append(deck.pop())

    choice =  ""

    # Player phase
    while (choice != "s"):
        player_points = calculate_hand_value(player)
        dealer_points = calculate_hand_value(dealer)

        print("Player hand: " + str(player) + " Points: " + str(player_points))
        print("Dealer hand: " + str(dealer) + " Points: " + str(dealer_points))
        print("")

        # fake it
        #player_points = 21

        # if player's hand is exactly 21
        if player_points == 21:
            print("Blackjack! You win!")
            playerWin += 1
            return bet * 2

        # if player's hand value is more than 21
        if player_points > 21:
            print("Bust! You lose.")
            dealerWin += 1
            return 0


        choice = input("To hit, enter \"h\". To stand, enter \"s\": ")

        if (choice == "h"):
            player.append(deck.pop())
            continue
        elif (choice == "s"):
            break
        else:
            print("Enter only either 'h' or 's'.")
            continue

    # Dealer phase
    while dealer_points < 17:
        dealer.append(deck.pop())
        dealer_points = calculate_hand_value(dealer)
        print("Dealer draws... New hand: " + str(dealer) + " Points: " + str(dealer_points))

    dealer_points = calculate_hand_value(dealer)
    # Fake it
    #dealer_points = 21

    # if dealer's hand is exactly 21
    if dealer_points == 21:
        print("Dealer blackjack! You lose.")
        dealerWin += 1
        return 0
    if dealer_points > 21:
        print("Dealer bust! You win!")
        playerWin += 1
        return bet * 2


    # Just example and quick code. can be improved for reading
    if player_points > dealer_points:
        print("You win!")
        playerWin += 1
        return bet * 2
    elif dealer_points > player_points:
        print("Dealer wins.")
        dealerWin += 1
        return 0
    else:
        print("It's a draw.")
        return bet

def main():
    bet = 0
    player_funds = 1000

    while True:
        print(f"Player wins: {playerWin}")
        print(f"Dealer wins: {dealerWin}")
        print(f"\nAvailable funds: {player_funds}")
        print("Bet 0 to quit.")
        # Takes the player's bet amount
        bet = int(input("Enter your bet amount: "))
        if bet <= 0:
            break
        while bet > player_funds:
            print("Insufficient funds!")
            bet = 0
            bet += int(input("Enter your bet amount: "))
        player_funds -= bet

        player_funds += blackjack(bet)

        if player_funds == 0:
            print("Out of money! You lose!")
            break

main()
