# print("========Student Result=========")
num_of_students = int(input("Enter number of students: "))
increment = 1
student_marks = []
while increment <= num_of_students:
    print(f"==========Student Roll NUmber:  {increment} ==============")
    for mark in range(1):
        nep = int(input("Enter marks of Nepali: "))
        eng = int(input("Enter marks of English: "))
        math = int(input("Enter marks of Math: "))
        sci = int(input("Enter marks of Science: "))
        sst = int(input("Enter marks of Social Studies: "))
        get_mark = [nep, eng, math, sci, sst]
        student_marks.append(get_mark)
    increment += 1

student_number = 1
for student in student_marks:
    total_mark = 0
    for mark in student:
        total_mark += mark

    percentage = total_mark / 5
    division = ''

    if percentage > 35 and percentage <= 45:
        division = 'Third'
    elif percentage > 45 and percentage <= 60:
        division = 'Second'
    elif percentage > 60 and percentage <= 80:
        division = 'First'
    elif percentage > 80 and percentage <= 100:
        division = 'Distinction'
    else:
        division = 'Fail'

    print(
        f"Student Roll Number: {student_number} Total Marks: {total_mark} Percentage: {percentage} Division: {division}")

    student_number += 1
