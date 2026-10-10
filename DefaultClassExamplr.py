class Example:
    pass

example_1 = Example()
example_1.id="001"
example_1.name="Sample Example"
print(example_1.id)
print(example_1.name)



class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

user = User("Trello",56)
print(f"user name is {user.name}")
print(user.greet())