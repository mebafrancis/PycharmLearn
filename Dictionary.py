dictionary_content={"Bug":"A software error, an error in the program that causes it to behave in an undesirable way.",
"Code" : "A set of instructions written in a programming language.",
"Algorithm" : "A step-by-step plan for solving a problem.",
"Data Structure" : "A data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to them.",
"Function" : "A block of code that performs a specific task."}

print(dictionary_content)
print(dictionary_content["Bug"])

dictionary_content["Loop"]="A programming construct that allows code to be executed repeatedly until a certain condition is met."

print(dictionary_content)

for key in dictionary_content:
    print(key, dictionary_content[key])

capitals={"USA":"Washington D.C.", "India":"New Delhi", "United Kingdom":"London"}
travel_log={"USA":["New York City", "Washington D.C.", "Boston"], "India":["Mumbai", "Delhi", "Bangalore"]}
print(travel_log)
print(travel_log["USA"][1])

nested_list=[[1,2,3], [4,5,6], [7,8,9]]
print(nested_list[1][1])

new_travel_log ={
    "France":{
        "num_times_visited": 2,
        "cities_visited": ["Paris", "London"],
        "is_returning": True
    }
    ,
    "USA":{
        "num_times_visited": 3,
        "cities_visited": ["New York City", "Washington D.C.", "Boston"],
        "is_returning": False
    }
}
print(new_travel_log["France"]["cities_visited"][1])