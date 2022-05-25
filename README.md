# Inspire.in.STEM
# Inspire.in.STEM
# Inspire.in.STEM
#####
# git commands
git add *
git add lesson4.py
git commit -m "lesson about"
git branch -m
git config --global user.name="EddyMwai"
git config --global user.name="mwaikimemia@gmail.com
git remote add

# DICTIONARIES
what are dictionares
syntax of dictionaries
define , add ,remove, accessing
looping ove dictionaries
dic in dic, list in dic,dic in lists

 # ERRORS
  Syntax
  Indentation

#  #############################
#           Dictionaries    #
#          Name : Eddy Mwai
#   Date : 23 / 5 / 20
# ####################################
#A dictionary is a collection of key value pairs
#syntax:dictionary = ['key':'value']
name = 'john'
colours={'colour':'red'}
vehicle={'type':'toyota', 'plate_number':'kny316'}
#print(type(colours)) to read the data type : we use the type method


# Initializing dictionaries
student = {"Name":"Memz", "age":24, "sex":"Male"}
print(student["Name"])
print(student["sex"])
print(student["age"])

# adding an item in the dictionary
student["Id_No"] = "21250"
student["club"] = "Mancity"
student["sport"] = "fotball"
print(student)

# starting with an empty dictionary
student1 = {}

# add pairs
student1["fav_food"] = "turkey"
student1["home_city"]="Nairobi"
print(student1)

# modifying values in a dictionary
student["age"] = "18"
print(student["age"])

# removing an element
del student1["fav_food"]
print(student1)
