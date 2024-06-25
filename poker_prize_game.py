import random

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(rank + ' of ' + suit)
print(deck)

# Shuffle the deck
random.shuffle(deck)

# Deal 5 cards to each player
player1_hand = deck[:5]
player2_hand = deck[5:10]

# Display the hands
print("Player 1's hand:")
print(player1_hand)
print("Player 2's hand:")
print(player2_hand)

# Function to determine the hand rank
def get_hand_rank(hand):
    # Count the number of each rank
    rank_counts = {}
    for card in hand:
        rank = card[0]
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1

    # Determine the hand rank
    hand_rank = 0
    for rank, count in rank_counts.items():
        if count == 4:
            hand_rank = 1
        elif count == 3:
            hand_rank = 2
        elif count == 2:
            hand_rank = 3
        elif count == 1:
            hand_rank = 4
    return hand_rank   

 # Determine hand ranks
player1_hand_rank = get_hand_rank(player1_hand)
player2_hand_rank = get_hand_rank(player2_hand)

 # Display the hand ranks
print("Player 1's hand rank:", player1_hand_rank)
print("Player 2's hand rank:", player2_hand_rank)

 # Determine the winner
if player1_hand > player2_hand:
   print("Player 1 wins!")
   player1_cash_prize = 100
   player2_cash_prize = 0
elif player1_hand < player2_hand:
   print("Player 2 wins!")
   player1_cash_prize = 0
   player2_cash_prize = 100
else:
   print("It's a tie!")
   player1_cash_prize = 50
   player2_cash_prize = 50
     
# Award cash prize to the winner
print("Player 1's cash prize:", player1_cash_prize)
print("Player 2's cash prize:", player2_cash_prize)
print("Thank you for playing!")



    
    



        


            