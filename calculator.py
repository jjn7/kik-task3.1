#create standard definitions of add, substract, divide and multiply

def add(a, b):
        return a + b

def subtract(a, b):
        return a - b

def divide(a, b):
        return a / b

def multiply(a, b):
        return a * b

#requst user input
#input() collectes what the user types - note: input() is alwasy a string by default
num1 = input("Enter the first number: ")
num2 = input("Enter the second number")
operation = input("Choose an operation (+, -, /, *): ")