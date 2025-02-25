# 7. Write a while loop to print the first 5 multiples of 3

num = int(input(" Enter a number to print its multiples : "))
count = 1
multiple = num
while count <= 5:
    print(multiple)
    multiple += num  
    count += 1
