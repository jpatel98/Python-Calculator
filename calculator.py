# program to make a simple calculator

#function to add
def add(x, y):
    return x + y

#function to subtract
def subtract(x,y):
    return x - y

#function to multiply
def multiply(x, y):
    return x * y

#function to divide
def divide(x, y):
    return x / y

#printing operation option to user.
print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    #getting input for choice
    choice = input("Enter choice (1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    
    else:
        print("Invalid Input")
