#! /usr/bin/python

#to print even numbers ...use modullas%
#for number in range(0,10):      

#prod of all odd no's btwn 1 and 20
product = 1
for number in range(1,20):
    if (number % 2 == 1):
        product = product * number
#print(product)

#calcullate the factorial of 6
product=1
#for number in range (1,7):
    #product = product * number
#print(product)
fact= number * (number-1)

##################################
# WHILE LOOP

num = 10
while num < 10:
    if(num % 2 == 0):
      print(num)
num=num + 1