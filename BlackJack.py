import random

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

user_card = []
computer_card = []
is_gameover = False
dealer_score = -1
user_score = -1

def calculate_score(card_list):
    score=sum(card_list)
    if score == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
    return score

def compare(u_score, d_score):
    if u_score == d_score:
        return "DRAW"
    elif d_score == 0:
        return "YOU WIN!"
    elif u_score == 0:
        return "WIN WITH Blackjack!"
    elif u_score > 21:
        return "Went over 21 !You Lose"
    elif d_score > 21:
        return "Opponent went over 21! you win"
    elif u_score > d_score:
        return "You win!"
    else:
        return "You Lose!"

print("Welcome to Blackjack!")
for draw in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

while not is_gameover:
    user_score = calculate_score(user_card)
    dealer_score = calculate_score(computer_card)
    print(f"Your cards: {user_card}, Score: {user_score}")
    print(f"Computer's first card: {computer_card[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21 or dealer_score > 21:
        is_gameover = True
    else:
        user_input = input("Do you want to hit or stand? (h/s): ")
        if user_input.lower() == "h":
            user_card.append(deal_card())
        else:
            is_gameover = True

while dealer_score !=0 and dealer_score < 17:
    computer_card.append(deal_card())
    dealer_score = calculate_score(computer_card)

print(compare(user_score, dealer_score))
print(f"Your cards: {user_card}, Score: {user_score}")
print(f"Computer's cards: {computer_card}, Score: {dealer_score}")