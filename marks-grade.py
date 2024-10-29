marks = int(input("Enter your marks:"))

if marks > 79:
    grade = "A+"
elif marks > 69 and marks < 80:
    grade = "A"
elif marks > 59 and marks < 70:
    grade = "A-"
elif marks > 49 and marks < 60:
    grade = "B"
elif marks >39 and marks < 50:
    grade = "C"
else:
    grade = "F"

print(f"your grade is {grade}")
    
