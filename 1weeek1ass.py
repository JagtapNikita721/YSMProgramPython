# 1. Write a program to find the largest of two numbers using if-else statements.

num1 = float(input("Enter the First Number : "))
num2 = float(input("Enter the Second Number : "))

if num1 > num2 :
    print(f" The Largest nmuber is {num1}")
elif num2 > num1 :
    print(f" The Largest Number is {num2}")
else :
    print(" The both numbers are equal")