import StudentScores
# program to take in student scores and calculate their grades based on metrics (from lab)

student_grades = {}

def calc_grades(student_scores):
    for key in student_scores:
        if 91 <= student_scores[key] <= 100:
            student_grades[key] = "Outstanding"
        if 81 <= student_scores[key] <= 90:
            student_grades[key] = "Exceeds Expectations"
        if 71 <= student_scores[key] <= 80:
            student_grades[key] = "Acceptable"
        elif student_scores[key] <= 70:
            student_grades[key] = "Fail"
         
    return student_grades

student_grades = calc_grades(StudentScores.student_scores)
print(student_grades)