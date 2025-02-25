# 3. Write a function is_even(n) that returns True if a number is even, otherwise False.

def is_even(n):
    return n % 2 == 0
input = int(input(" Enter a number to check if it's even : "))
result = is_even(input)

if result:
    print(f"{input} is even.")
else:
    print(f"{input} is not even.")

