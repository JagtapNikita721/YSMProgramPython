#10. Write a program that checks if a year is a leap year. (Hint: A year is a leap year if it is divisible by 4 but not by 100, 
# except when it is also divisible by 400.

year = int(input(" Enter a year to check if it's a leap year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
