# 8. Create a loop that prints all numbers from 1 to 20 but skips multiples of 5.

upper_limit = int(input(" Enter the upper limit to print numbers : "))

for num in range(1, upper_limit + 1) :
    if num % 5 == 0:
        continue  
    print(num)
