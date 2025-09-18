import random

EASY_LEVEL=10
HARD_LEVEL=5

def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level=="easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_answer(user_guess,my_num,turns):
    if user_guess>my_num:
        print("Too High")
        return turns-1
    elif user_guess<my_num:
        print("Too Low")
        return turns-1
    else:
        print("You got it right")
        return -1

def game():
    print("Welcome to num guessing game!!")
    my_num = random.randint(1, 50)
    turns=set_difficulty()
    print(f"You have {turns} attempts to guess the number")

    guessNum=0
    while guessNum!=my_num and turns>0:
        print(f"You have {turns} attempts remaining to guess the number")
        guessNum=int(input("Enter your guess"))
        turns=check_answer(guessNum,my_num,turns)
game()






