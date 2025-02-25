#2. Create a function square(num) that returns the square of a given number.
def square(num):
    return num ** 2

input = float(input(" Enter a number to square : "))
result = square(input)
print(f" The square of {input} is {result} ")
