#! /usr/bin/python
######################################
#write a program to withdraw ksh25Gs if account balance is btw 100Gs to 200Gs
#30% if acc balance is btwn 500Gs to 1M
#Above 1M deduct 15000
#######################################
acc_balance=input("What is your account balace?")
if (int(acc_balance)>100000) and (int(acc_balance)<200000):
    acc_balance=int(acc_balance) - 25000
    print("You have withdrawn 25000.")
elif (int(acc_balance)>500000) and (int(acc_balance)<1000000):
    acc_balance=int(acc_balance) - (0.3*int(acc_balance))
    print("We have deducted 30 percent from your account.")
elif int(acc_balance)>1000000:
    acc_balance=int(acc_balance) - 15000
    print("We have deducted 15000 from your acc.")
else :
    print("No money deductions on your account.")