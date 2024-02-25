import random
import time

def card_deal(player_hand):
    cards = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
             'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

         # how to assign value to character cards?
         # how to allow aces multiple values?

    card_name = random.choice(list(cards.keys()))
    if card_name == 'Ace':    # is player's hand > 10?
        if sum(player_hand) + 11 > 21:
            return 1  # return 1 if ace makes > 21
        else:
            return 11  # otherwise add 11
    else:
        return cards[card_name]

    player_hand = []
    card_value = card_deal(player_hand)
    if card_value == 1:
        print("Dealt an Ace with value 1")
    else:
        print("Dealt an Ace with value 11")

def compare(user_sum, dealer_sum):
                              
                              #snarky dealer responses
    dealer_win_responses = [         
    " The House always wins.",
    " Better luck next time.",
    " In your face, loser!"   
    ]
    
    
    if user_sum == dealer_sum:
        return "Draw"
    elif user_sum == 21:
        return "21! Blackjack!"
    elif dealer_sum == 21:
        return "Dealer wins!" + random.choice(dealer_win_responses)
    elif user_sum > 21:
        return "Bust!"
    elif dealer_sum > 21:
        return "Dealer bust. You win!"
    elif user_sum > dealer_sum:
        return "Winner!"
    else:
        return "Dealer wins!" + random.choice(dealer_win_responses)
        
        
        
        
        

def sum_score(cards): #
    
    score = 0
    for card in cards:
        if card in ('Jack', 'Queen', 'King'):
            score += 10
        elif card == 'Ace':
            score += 11
        else:
            score += int(card)
    
    num_aces = cards.count('Ace') 
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score

def game_play():
    print("--------------Blackjack!---------------\nGet as close to 21 without going over")
   
    rounds = 0  

    while rounds < 3:  # loop 3 rounds
        game_over = False
        dealer_cards = []
        player_cards = []

        for x in range(2):
            dealer_cards.append(card_deal(dealer_cards))
            player_cards.append(card_deal(player_cards))

        while not game_over:
            player_score = sum_score(player_cards)           #display first hand
            dealer_score = sum_score(dealer_cards)
            print(f"\nPlayer Hand: {player_cards}, current score: {player_score}")
            print(f"Dealer's Hand: [{dealer_cards[0]}, ?]")
            time.sleep(.5) #slow the speed outputs are displayed, for comfort
            if player_score >= 21:
                break    

            player_input = input("Would you like to 'hit' or 'stay'? ").lower()   # player move
            if player_input == 'hit':
                player_cards.append(card_deal(player_cards))
            elif player_input == 'stay':
                break

        while sum_score(dealer_cards) < 17:      # dealer must hit until score > 17
            dealer_cards.append(card_deal(dealer_cards)) 
        
#pause for dramatic effect?
        print(f"\nPlayer's final cards: {player_cards}, Player's Score: {sum_score(player_cards)}")
        print(f"Dealer's final cards: {dealer_cards}, Dealer's Score: {sum_score(dealer_cards)}") 
        print(compare(sum_score(player_cards), sum_score(dealer_cards)))  # display final hand and scores
        time.sleep(1.5)
        
        rounds += 1       #add 1 to round count

    game_play_again = input("Do you want to keep losing your money? (yes or no): ").lower()
    if game_play_again == "yes": 
        game_play()      # restart 3 rounds
    else: 
        game_over = True
game_play() #start

