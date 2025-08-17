import random

computer_choice = random.choice(["rock", "paper", "scissors"])
input_value=input("What do u choose?0 for rock 1 for paper 2 for scissors\n")
if input_value not in ['0', '1', '2']:
    print("Invalid input. Please enter 0, 1, or 2.")
    exit()

if int(input_value) == 0:
    choice = "rock"
elif int(input_value) == 1:
    choice = "paper"
else:
    choice = "scissors"
    
print(f"You chose {choice}.")
print(f"Computer chose {computer_choice}.")

if choice == computer_choice:
    print("It's a tie!")
elif (choice == "rock" and computer_choice == "scissors") or (choice == "paper" and computer_choice == "rock") or (choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
