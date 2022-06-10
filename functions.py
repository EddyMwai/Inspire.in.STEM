
 # Functions is a block of code which gets executed together
 # Initializing functions/definition of a function
def say_hello():
    print("Hello from JKUAT")
    x=4
    y=7
    z=x+y
    print(z)
# Calling functions
say_hello()

def bark():
    print("Dogs bark woof woof")
bark()
def moo():
    print("Cows moo")
moo()
def hiss():
    print("Snakes hiss ssss")
hiss()

########################################
# Function parameters
# A function to add numbers
def add_numbers (x,y):
    sum_nums=x+y
    print("The sum of thenumbers is:",sum_nums)
add_numbers(40,50)
def hiss():
    print("Snakes hiss ssss")
hiss()

#########################################
# Function parameters
# A function to add numbers
def add_numbers(x,y):
    sum_nums=x+y
    print("The sum of the numbers is:", sum_nums)
add_numbers (40,50)
add_numbers (100,400)
add_numbers (1,4)
# A function to multiply numbers
def multi_numbers (x,y):
    prod_numbers=x*y
    print("The product of numbers is:", prod_numbers)
multi_numbers(20,3)
multi_numbers(50,70)

###########################################3
#using default parameters
def print_name(name="Memz"):
    print(name)
print_name("Eddy")

#return from a function
def get_sum(num1, num2):
    sum_nums=num1+num2
    return sum_nums
print(get_sum(7,12)) 

#write a function that gets the square of numbers
def powers(number,power):
    pow_numb=number**power
    return pow_numb

print(powers(6,4))

def get_full_name(f_name, s_name):
    full_name=f_name+" "+ s_name
    return full_name.title()
print(get_full_name("Eddy","Memz"))

#returning a dictionary from a function
def create_full_name(f_name,s_name):
    person={'first':f_name,'second':s_name}
    return person
student=create_full_name('Eddy','Memz')
print(student)

#passing a list in a function
def greet_friends(names):
    for name in names:
        msg=("Hello "+ name.title()+" !")
        print(msg)
friends=['Bob','Shantal','Shawn']
greet_friends(friends)