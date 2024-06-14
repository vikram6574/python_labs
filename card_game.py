# python code to deal random card 

import random
# Define the card suits, ranks, and create a deck
suits = ['Hearts', "Diamonds", "Spades", "Clubs"]
ranks = ['2', "3", "4", "5", "6", "J", "Q", "K", "A"]
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(rank + ' of ' + suit)
print(deck)

# Shuffle the deck
random.shuffle(deck)    

# Deal a hand of 5 cards
hand = random.sample(deck, 5)
print(hand)

# Print the hand of cards
for card in hand:
    print(card)
    

        

    