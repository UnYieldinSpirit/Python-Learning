student_scores = [150, 142, 185, 120, 171, 184, 149, 178, 98, 78, 69]

sum_student_scores = 0
max_score = 0

# for Loop used to calculate the sum of a list
for score in student_scores:
    sum_student_scores += score

for score in student_scores:
    if score > max_score:
        max_score = score

# built-in sum function that can calculate the sum of things
total = sum(student_scores)

print(f"The max score of the student scores is: {max_score}")
print(f"The sum of the student scores is: {sum_student_scores}")
