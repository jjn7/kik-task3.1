#create standard definitions of add, subtract, divide and multiply
def add(a, b):
        return a + b

def subtract(a, b):
        return a - b

#python cannot handle a number divided by zero becuase it's unlimited and would not finish compututing the answer
#function to return error message when dividing number by zero
def divide(a, b):
        if b == 0:
                return "Error: cannot divide by zero" #if this runs, it exits the function
        return a / b

def multiply(a, b):
        return a * b

#create loop to continue requesting new calculations
while True: #boolean
# Ask if user wants to do a calculation
        again = input("Do you want to do a calculation? (y/n): ").lower()
        if again != 'y':
                print("End of calculation")
                break
    
#request user input
#input() collects what the user types - note: input() is always a string in python
        first_input = input("Enter the first number: ")
        second_input = input("Enter the second number: ")
        operation = input("Choose an operation (+, -, /, *): ")

        try:
#convert the string to float and assigns it to the variable num1 or num2
                num1 = float(first_input)
                num2 = float(second_input)
        except ValueError: #catch the error if occurs: in this case, not a number
                print("Invalid input, numbers only.\n")
                continue

#use selection construct to determine user input
        if operation == '+':
                result = add(num1, num2)
        elif operation == '-':
                result = subtract(num1, num2)
        elif operation == '/':
                result = divide(num1, num2)
        elif operation == '*':
                result = multiply(num1, num2)
        else: result = "Invalid operation"

        print("Result:", result)

#check if user wants to complete another calculation
#        again = input("Do you want to do another calculation? (y/n): ").lower() #.lower() ensures that the letter is turned into lowercase
 #       if again != 'y':
  #              print("End of calculation")
    #            break