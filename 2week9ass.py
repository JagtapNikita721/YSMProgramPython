# 9. Write a loop that stops when it encounters the number 7 in this list: [1, 2, 3, 4, 5, 6, 7, 8, 9].

user_input = input(" Enter a list of numbers separated by spaces : ")
numbers = [int(num) for num in user_input.split()]

for num in numbers:
    if num == 7:
        print("Encountered number 7,  so stopping the loop.")
        break
    print(num)
