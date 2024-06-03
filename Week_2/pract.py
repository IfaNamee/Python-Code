import random

def main():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    print(f"Your hand: {player_hand}")
    print(f"Dealer's hand: {dealer_hand[0]}")

    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)

    while player_score < 21:
        action = input("Do you want to hit or stand? (h/s): ")

        if action == "h":
            player_hand.append(deck.pop())
            player_score = sum(player_hand)
            print(f"Your hand: {player_hand}")
        elif action == "s":
            break

    while dealer_score < 17:
        dealer_hand.append(deck.pop())
        dealer_score = sum(dealer_hand)

    print(f"Your hand: {player_hand}")
    print(f"Dealer's hand: {dealer_hand}")
    print(f"Your score: {player_score}")
    print(f"Dealer's score: {dealer_score}")

    if player_score > 21 or (dealer_score <= 21 and dealer_score > player_score):
        print("Dealer wins!")
    elif dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
