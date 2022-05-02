from re import L


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# max()
highest_score = 0
for loop_score in range(0, len(student_scores)) :
    if student_scores[loop_score] > highest_score :
        highest_score = student_scores[loop_score]
print(f"The highest score is: {highest_score}")