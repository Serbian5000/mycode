import random

def card_value(card):
    if card in ('Jack', 'Queen', 'King'):
        return 10
    elif card == 'Ace':
        return 11
    else:
        return int(card)

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return random.choice(cards)

def calculate_score(hand):
    score = sum(card_value(card) for card in hand)
    num_aces = hand.count('Ace')
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score

def print_hand(hand, hidden=False):
    if hidden:
        print("Hidden card, ", end="")
        print(hand[1])
    else:
        print(", ".join(hand))

def blackjack():
    print("Welcome to Blackjack!")
    while True:
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]

        print("Your hand:")
        print_hand(player_hand)
        print("Dealer's hand:")
        print_hand(dealer_hand, hidden=True)

        # player's turn
        while True:
            player_score = calculate_score(player_hand)
            if player_score == 21:
                print("Blackjack! You win!")
                break
            elif player_score > 21:
                print("Bust! You lose, idiot.")
                break

            action = input("Do you want to hit or stay? (hit/stay): ").lower()
            if action == 'hit':
                player_hand.append(deal_card())
                print("Your hand:")
                print_hand(player_hand)
            elif action == 'stay':
    

        # dealer's turn
        dealer_score = calculate_score(dealer_hand)
        while dealer_score < 17:
            dealer_hand.append(deal_card())
            dealer_score = calculate_score(dealer_hand)

        print("Dealer's hand:")
        print_hand(dealer_hand)
        if dealer_score > 21:
            print("Dealer bust! You win!")
        elif dealer_score > player_score:
            print("Dealer wins! In your face loser!")
        elif dealer_score < player_score:
            print("You win!")
        else:
            print("Draw")

        play_again = input("Do you want to play again? (yes/no): ").lower()              #use lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    blackjack()
 
