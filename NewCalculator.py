def format_name(f_name,l_name):
    return f"{f_name.title()} {l_name.title()}"

print(format_name("melba","FRANCISCO"))

print("Welcome to calculator")
def addfunction(a, b):
    return a + b
def subtractfunction(a, b):
    return a - b
def multiplyfunction(a, b):
    return a * b
def dividefunction(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

operations = {"+": addfunction, "-": subtractfunction, "*": multiplyfunction, "/": dividefunction}
op_symbol=input("Enter the operation: ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

if op_symbol in operations:
    print(operations[op_symbol](num1, num2))
else:
    print("Invalid operation")


