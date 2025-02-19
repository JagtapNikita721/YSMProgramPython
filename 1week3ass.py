# 3. Write a program that checks whether a given number is even or odd using the ternary operator.

num = int(input(" Enter a number :  "))
result = "Even" if num % 2 == 0 else "Odd"
print(f" The number {num} is {result}")
