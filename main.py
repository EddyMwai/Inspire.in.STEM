#!/usr/bin/python
#########################################
#   Name:Eddy Mwai
#   File:main.py
#   Date:6/06/22
#########################################


import operations
from student import student
from teachers import Teachers

print (operations.add_numbers(3,5))
print (operations.subtract_numbers(7,3))
print (operations.multiply_numbers(5,2))
print (operations.divide_numbers(10,2))

new_student = student("Memz", "cycling", "2000")

new_teacher = Teachers("Mr John","13000","literature","54000")
print(new_teacher.get_tsc_no())

student.greet_student()
print(student)