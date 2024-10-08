# CTI 110
# P1HW1
#CYBER HANK
# 10/8/24
#write mathmatical code


# Function to perform mathmatic operations
def simple_math(a, b):
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    # Check if b is not zero before division to avoid division by zero error
    if b != 0:
        print(f"Division: {a} / {b} = {a // b}")  # Integer division
    else:
        print("Division: Cannot divide by zero")

# Input two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Call the function with the input integers
simple_math(num1, num2)

print("-" *7, "Calculating Exponents", "-" *13)
base=int(input("Enter an integer as the base value:"))
exponents=int(input("Enter an integer as an exponents:"))
answer= base ** exponents
print(base, "raised to the power of ",exponents,"is",answer,"!")
print("-" *7, "Addition and Subtraction", "-" * 5)
first=int(input("Enter an starting integer:"))
second=int(input("Enter an integer to add:"))
third=int(input("Enter an integer to subtract:"))
answer = first + second - third
print(answer)
print(first, "+", second, "-", third, "=", answer)
