from grades import *
from status import *

name = input("Enter student name: ")

grades_list = [11, 20]

average = avg(grades_list)
maximum = max_grade(grades_list)
minimum = min_grade(grades_list)

result = check_status(average)

print("Student:", name)
print("Avg =", average)
print("Max =", maximum)
print("Min =", minimum)
print("Status =", result)