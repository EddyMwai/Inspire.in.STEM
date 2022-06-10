#!/usr/bin/python
################################
#  Name:Eddy Mwai
#  Date:08/06/2022
#  palidrome.py
##################################
#to check if a word is a palindrome
def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
s = input("what is the number?")
ans = isPalindrome (s)
if (ans):
    print("it is")
else:
    print("tis not")

