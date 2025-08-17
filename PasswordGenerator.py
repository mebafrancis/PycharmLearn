import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol=['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+']

print("Welcome to the Random Password Generator!")
nr_letters = int(input("Enter the number of letters: "))
nr_numbers = int(input("Enter the number of numbers: "))
nr_symbols = int(input("Enter the number of symbols: "))

#easy Level
password=""
for char in range(nr_letters):
    password += random.choice(letters)
for num in range(nr_numbers):
    password += random.choice(numbers)
for sym in range(nr_symbols):
    password += random.choice(symbol)
print("Easy Level Password: ", password)

#Hard Level
password_list=[]
for char in range(0,nr_letters):
    password_list+= random.choice(letters)
for num in range(0,nr_numbers):
    password_list+= random.choice(numbers)
for char in range(0,nr_symbols):
    password_list+= random.choice(symbol)
print("Hard Level Password: ",password_list)
random.shuffle(password_list)
print("Shuffled password",password_list)