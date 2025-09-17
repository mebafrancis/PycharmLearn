game_level=3
enemies=["Alien","Zombie","Skeleton"]
#No scope i if and while loops
if game_level<5:
    new_enemy=enemies[1]

print(new_enemy)

enemiesScope=1

def increase_enemies():
    global enemiesScope
    enemiesScope+=1
    print(f"enemies inside function : {enemiesScope}")

increase_enemies()
print(f"enemies outside function : {enemiesScope}")

#Global Constants
PI = 3.14159

def my_func():
    print(PI)
my_func()