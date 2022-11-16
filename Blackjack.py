############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random 
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  x = random.randint(0,12)
  return cards[x]


def calculate_score(cards):
  if cards[0]== 11 or cards[1]==11:
    if sum(cards)>=21:
      return sum(cards)-10
    return 0
  else:
    return sum(cards)


def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  for i in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over :
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
  
    print(f"Your cards are :{user_cards} & current score : {user_score}")
    print(f"Computer's first card : {computer_cards[0]}")
  
    if user_score == 0 or computer_score == 0 or user_score>21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card or type 'n' to pass : ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final cards are :{user_cards} & final score : {user_score}")
  print(f"Computer's final cards : {computer_cards}")
  print(compare(user_score,computer_score))


while input("Do you want to play Blackjack? Type 'y' for yes & 'n' for no :") == 'y':
  clear()
  play_game()
    
