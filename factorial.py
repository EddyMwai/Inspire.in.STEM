number = int(input("Enter the number"))
factorial = 1
if number<0:
    print("Factorial of negative no's does not exist")
elif number==0:
    print("Factorial of 0 is 1") 
else:
    for i in range(1,number+1):   
        factorial=factorial*i
print("Factorial of number :", factorial)
