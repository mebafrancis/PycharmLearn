import random
import MyModule

rand_int=random.randint(1,10)
print(rand_int)
print(MyModule.my_value)

ran_float= random.random()
print(ran_float)

ran_float_other=random.uniform(1,10)
print(ran_float_other)

rand_head_tail=random.randint(0,1)
if rand_head_tail==1:
    print("Heads")
else:
    print("Tails")