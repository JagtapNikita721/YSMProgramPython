 # 10. Write a program that prints the grade based on the score input using if-else statements (A for 90-100, B for 80-89, etc.).

score = int(input(" Enter your score : "))
if 90 <= score <= 100 :
    grade = 'A'
elif 80 <= score < 90 :
    grade = 'B'
elif 70 <= score < 80 :
    grade = 'C'
elif 60 <= score < 70 :
    grade = 'D'
elif 50 <= score < 60 :
    grade = 'F'
else :
    grade = "Invalid Score "

print(f" Your GRADE is : {grade}")