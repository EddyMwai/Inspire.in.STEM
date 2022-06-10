import random
print('Welcome to our password generator')
character ='kdb17'
#ask number of pw
number_of_passwords=int(input("How many passwords:"))
#ask user for pw length
length_of_password=int(input("How long are the passwords:"))
print('/n Here are your passwords.')
for password in range (number_of_passwords):
    password=''
    for c in range(length_of_password):
        password+=random.choice(character)
    print(password)

#covert into class
class Password:
    