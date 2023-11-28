# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))
#convert the input to integer
exam_two = int(input("Input exam grade two: "))
#the input was converted to an integer and the variable was changed to exam_three from exam_3
exam_three = int(input("Input exam grade three: "))
#added comas to grades
grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades: #the list variable was changed from grade into grades 
  sum = sum + grade
#spelling mistake for grades 
avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #colon was missing 
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" # the single qoutation was changed into double qoutations 
elif avg <= 69 and avg >= 70: # changed the value from 65 to 70 
    letter_grade = "D"
else: #elif command changed into else 
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F": # letter-grade was changed to _ and removed is and put ==
    print ("Student is failing.") #added missing brackets 
else:
    print ("Student is passing.")#missing brackets added 
