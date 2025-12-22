student_marks ={"Anand":85,"geetha":98}
'''
for marks in student_marks:
    print(marks)

for marks in student_marks.keys():
    print(marks)

for marks in student_marks.values():
    print(marks)
'''
for student,marks in student_marks.items():
    print(f"{student}={marks}")

