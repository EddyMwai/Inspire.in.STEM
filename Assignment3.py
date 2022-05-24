#write a program that gets user input and add ksh 10k to her acc if she is btwn  25 and 30 years
age=input("What is your age?")
acc_balance=0
if (int(age)>25) and (int(age)<30):
    acc_balance =acc_balance + 10000
    print("Confirmed You have received Ksh 10000")
else:
    print("Sorry no money for you")        


