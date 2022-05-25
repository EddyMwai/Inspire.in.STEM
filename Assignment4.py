#! /usr/bin/python
######################################
#write a program to withdraw ksh25Gs if account balance is btw 100Gs to 200Gs
#30% if acc balance is btwn 500Gs to 1M
#Above 1M deduct 15000
#######################################
acc_balance=input("What is your account balace? ")
if (float(acc_balance)>100000) and (float(acc_balance)<200000):
    new_acc_balance=int(acc_balance) - 25000
    print("You have withdrawn 25000.\nYou're acc balance is " + str(new_acc_balance))
elif (float(acc_balance)>500000) and (float(acc_balance)<1000000):
    new_acc_balance=float(acc_balance) - (0.3*float(acc_balance))
    print("We have deducted 30 percent from your account.\nYou're acc balance is " + str(new_acc_balance))
elif float(acc_balance)>1000000:
    new_acc_balance=float(acc_balance) - 15000
    print("We have deducted 15000 from your acc.\nYou're new balance is " + str(new_acc_balance))
else :
    print("No money deductions on your account.")