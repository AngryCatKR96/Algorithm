totalGrade = 0 
totalCredit = 0
for _ in range(20):
    subject, credit, grade = input().split()
    
    if grade == "A+":
        gradeScore = 4.5
    elif grade == "A0":
        gradeScore = 4.0
    elif grade == "B+":
        gradeScore = 3.5
    elif grade == "B0":
        gradeScore = 3.0
    elif grade == "C+":
        gradeScore = 2.5
    elif grade == "C0":
        gradeScore = 2.0
    elif grade == "D+":
        gradeScore = 1.5
    elif grade == "D0":
        gradeScore = 1.0
    elif grade == "F":
        gradeScore = 0
    elif grade == "P":
        continue
    
    totalCredit += float(credit)
    totalGrade += gradeScore * float(credit)

if totalCredit == 0:
    print(0.0)
else:
    print(totalGrade/totalCredit)