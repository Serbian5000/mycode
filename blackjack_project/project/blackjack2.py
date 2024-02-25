import random

def card_deal(player_cards):
    cards = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    card_name = random.choice(list(cards.keys()))
    if card_name == 'Ace' and sum(player_cards) >= 10:
        return 1
    else:
        return cards[card_name]

def score(cards):
    if sum(cards) == 21:
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

def compare(user_sum, dealer_sum):
    dealer_win_responses = [
        "The House always wins.",
        "Better luck next time.",
        "In your face, loser!"
    ]

    if user_sum == dealer_sum:
        return "Draw"
    elif user_sum == 21:
        return "21! Blackjack!"
    elif user_sum > 21:
        return "Bust!"
    elif dealer_sum > 21:
        return "Dealer bust. You win!"
    elif user_sum > dealer_sum:
        return "Winner!"
    else:
        return "Dealer Wins! " + random.choice(dealer_win_responses)

def game_play():
    print("-------------- Blackjack! ---------------\nGet as close to 21 without going over")

    cards = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    game_over = False
    dealer_cards = []
    player_cards = []

    for x in range(2):
        dealer_cards.append(card_deal(player_cards))
        player_cards.append(card_deal(player_cards))

    while not game_over:
        player_score = score(player_cards)
        dealer_score = score(dealer_cards)
        print(f"Player's Hand: {player_cards}, Your Score: {player_score}")
        print(f"Dealer's Hand: {dealer_cards[0]}, ?")

        player_input = input("Would you like to 'hit' or 'stay'? ").lower()
        if player_input == "hit":
            player_cards.append(card_deal(player_cards))
        elif player_input == 'stay':
            game_over = True

    while sum(dealer_cards) < 17:
        dealer_cards.append(card_deal(player_cards))

    print(f"Player's final hand: {player_cards}, Your Score: {score(player_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, Dealer's Score: {score(dealer_cards)}")
    result = compare(score(player_cards), score(dealer_cards))
    print(result)

game_play()
  
