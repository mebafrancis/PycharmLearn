
import random
from game_data import data
should_continue= True
while should_continue:
    randomA = random.choice(data)
    randomB = random.choice(data)
    print(randomA)
    print(randomB)
    guess = input(f"Guess who has more followers on instagram {randomA["name"] ,randomB["name"]}? Type 'A' or 'B': ").upper()
    if randomA["follower_count"] > randomB["follower_count"]:
        answer = 'A'
    else:
        answer = 'B'
    if guess != answer:
        should_continue= False
    else:
        should_continue=True
