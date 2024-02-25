#!/usr/bin/env python4
"""This is a final project CLI game of Blackjack"""

import random # randomizer utility



# Dealt cards
def card_deal(player_cards): 
    cards = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Jack':10,'Queen':10,'King':10,'Ace':11}
# how to assign value to name cards (dictionary?). 
# how to allow Aces two values?
    card_name = random.choice(list(cards.keys()))
    if card_name == 'Ace': # is player's hand is > 10
        if sum(cards) + 11 > 21:
            return 1  # Return 1 if Ace will > 21
        else:
            return 11  # Otherwise it's 11
    else:
        return cards[card_name]   
    
    




# calculates sum of each player's cards
def score(cards): 

    if sum(cards) == 21:
        
        if "Ace" in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)





# compare sums between dealer (compuer) and players
def compare(user_sum, dealer_sum): 
    dealer_win_responses = [
    "The House always wins.", 
    "Better luck next time.", 
    "In your face, loser!"   ]
    
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
        return "Dealer Wins!" +  random.choice(dealer_win_responses)
    

    



# How the game is played. Put options in lines(use dictionary)?
def game_play():
    print("--------------Blackjack!---------------\n Get as close to 21 without going over")

    cards = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Jack':10,'Queen':10,'King':10,'Ace':11}

    game_over = False
    dealer_cards = []
    player_cards = []

    for x in range(2):        
        dealer_cards.append(card_deal(cards))
        player_cards.append(card_deal(cards))

    while not game_over:
        player_score = sum(player_cards)
        dealer_score = sum(dealer_cards)
        print(f"Player's Hand: {player_cards}, Your Score: {player_score}")
        print(f"Dealer's Hand:{dealer_cards}, Dealer's Score: {dealer_score}")
                                                                             
        player_input = input("would you like to 'hit' or 'stay'?").lower() # use lower() to al

        if player_input == "hit":
            player_cards.append(card_deal(cards))
        elif player_input == 'stay':
            game_over = True
# pause?        
    while sum(dealer_cards) < 17:
        dealer_cards.append(card_deal(cards))

    print(f"Player's final hand: {player_cards}, Current Score: {sum(player_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, Current Score: {sum(dealer_cards)}")
    result = compare(sum(player_cards), sum(dealer_cards))
    print(result)


        
#    input("Do you want to playplay another hand? \nEnter 'Yes' or 'no'")
        
    # Do you want to play again?
game_play()








