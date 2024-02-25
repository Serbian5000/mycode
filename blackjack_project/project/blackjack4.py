import random

def card_deal(player_hand):
    cards = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
             'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    card_name = random.choice(list(cards.keys()))
    if card_name == 'Ace':
        # Check if the player's hand is over 10
        if sum(player_hand) + 11 > 21:
            return 1  # Return 1 if Ace will cause bust
        else:
            return 11  # Return 11 if Ace will not cause bust
    else:
        return cards[card_name]

player_hand = []
card_value = card_deal(player_hand)
if card_value == 1:
    print("Dealt an Ace with value 1")
else:
    print("Dealt an Ace with value 11")

def compare(user_sum, dealer_sum):
    if user_sum == dealer_sum:
        return "Draw"
    elif user_sum == 21:
        return "21! Blackjack!"
    elif dealer_sum == 21:
        return "Dealer wins!"
    elif user_sum > 21:
        return "Bust!"
    elif dealer_sum > 21:
        return "Dealer bust. You win!"
    elif user_sum > dealer_sum:
        return "Winner!"
    else:
        return "Dealer wins!"
        
        
        
        
        

def sum_score(cards):
    """Calculate the sum of the values of the cards in a hand."""
    score = 0
    for card in cards:
        if card in ('Jack', 'Queen', 'King'):
            score += 10
        elif card == 'Ace':
            score += 11
        else:
            score += int(card)
    # Adjust for Aces
    num_aces = cards.count('Ace')
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score

def game_play():
    print("--------------Blackjack!---------------\nGet as close to 21 without going over")
    
    game_over = False
    dealer_cards = []
    player_cards = []

    for _ in range(2):
        dealer_cards.append(card_deal(dealer_cards))
        player_cards.append(card_deal(player_cards))

    while not game_over:
        player_score = sum_score(player_cards)
        dealer_score = sum_score(dealer_cards)
        print(f"Player Hand: {player_cards}, current score: {player_score}")
        print(f"Dealer's Hand: [{dealer_cards[0]}, ?]")
        
        if player_score >= 21:
            break

        player_input = input("Would you like to 'hit' or 'stay'? ").lower()
        if player_input == 'hit':
            player_cards.append(card_deal(player_cards))
        elif player_input == 'stay':
            break

    while sum_score(dealer_cards) < 17:
        dealer_cards.append(card_deal(dealer_cards))
    
    print(f"Player's final hand: {player_cards}, Score: {sum_score(player_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, Score: {sum_score(dealer_cards)}")
    print(compare(sum_score(player_cards), sum_score(dealer_cards)))

    play_again = input("Do you want to play another hand? Enter 'Yes' or 'no': ").lower()
    if play_again == 'yes':
        game_play()
    else:
        print("Thanks for playing!")

# Start the game
game_play()
