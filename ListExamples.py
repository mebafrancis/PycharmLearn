import random

states_of_america=["Delaware","pennsylvania","Maryland","Virginia","North Carolina","South Carolina","Georgia",
                   "Florida","Alabama","Mississippi","Tennessee"]
print(states_of_america[0])
print(states_of_america[-3])
print(states_of_america)
states_of_america.append("New York")
print(states_of_america)
states_of_america.extend(["Indiana","Ohio"])
print(states_of_america)

fin_associates=["Cornell University","Stanford University","Harvard University","Yale University"]
print(fin_associates)
random_int=random.randint(0, len(fin_associates)-1)
print(fin_associates[random_int])