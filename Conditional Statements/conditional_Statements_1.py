# Grade students based on marks

marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks < 90 and marks >= 80:
    grade = "B"
elif marks < 80 and marks >= 70:
    grade = "C"
elif marks < 70 and marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Student get grade: ", grade)
