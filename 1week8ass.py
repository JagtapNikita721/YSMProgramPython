#8. Write a program to compare two numbers and print whether the first is greater, smaller, 
#or equal to the second using relational operators.

num1 = float(input(" Enter the First Number : "))
num2 = float(input(" Enter the Second Number :"))
if num1 > num2 :
    print(" The First number is greater than the second.")
elif num1 < num2 :
    print(" The first number is smalller than the second.")
else :
    print(" The first number is equal to the second number.")