# 6. Use a lambda function with filter( ) to get all even numbers from a list: [1, 2, 3, 4, 5, 6, 7, 8].

input = input("Enter numbers separated by space: ")
numbers = list(map(int, input.split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
