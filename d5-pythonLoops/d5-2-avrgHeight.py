student_heights = input("Input a list of student heights ").split(", ")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#átváltja intre az adatot

#total_height = sum(student_heights)
total_height = 0
for height in student_heights :
    total_height += height
print(total_height)

#number_of_students = len(student_heights)
number_of_students = 0
for student in student_heights : 
    number_of_students += 1
print(number_of_students)

avrg_height = round(total_height / number_of_students)


#solve it with no use of len() or sum()
#total_students_height = len(student_heights)
#total_students_sum = sum(student_heights)
#print(total_students_height)
#print(total_students_sum)
#total_height = sum(student_heights)
#number_of_students = len(student_heights)
#avrg_height = round(total_height / number_of_students)
#print(avrg_height)
