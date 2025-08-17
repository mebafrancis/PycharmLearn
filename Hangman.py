import random

word_list = ["apple", "banana", "orange", "pear", "kiwi", "mango"]
list_of_blank_words = []
randomWord = random.choice(word_list)
lifeValue = 6  # Standard hangman lives
hyphenChar = "_"

for letter in randomWord:
    list_of_blank_words.append("_")

print("Welcome to Hangman!")
print("Word to guess:", " ".join(list_of_blank_words))

while lifeValue > 0:
    guessed_letter = input("Guess a letter: ").lower()
    
    if guessed_letter in randomWord:
        print("Good guess!")
        for i in range(len(randomWord)):
            if randomWord[i] == guessed_letter:
                list_of_blank_words[i] = guessed_letter
        print("Current word:", " ".join(list_of_blank_words))
        
        # Check if word is complete
        if hyphenChar not in list_of_blank_words:
            print("Congratulations! You win!")
            break
    else:
        print("Incorrect guess. Try again.")
        lifeValue -= 1
        print(f"Lives remaining: {lifeValue}")
        print("Current word:", " ".join(list_of_blank_words))

if lifeValue == 0:
    print(f"You lost! The word was: {randomWord}")
