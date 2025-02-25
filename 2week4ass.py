# 4. Define a function sum_numbers(a, b=10) that takes two numbers and returns their sum. If the second number is not provided, 
# it should default to 10.
def sum_numbers(a, b=10):
    return a + b

a = float(input(" Enter the first number : "))
b = input(" Enter the second number (press Enter to use default 10) : ")

if b == "":
    result = sum_numbers(a)
else:
    b = float(b)
    result = sum_numbers(a,b)

print(f"The sum is: {result}")
