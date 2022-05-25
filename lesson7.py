
#############################
#           Dictionaries    #
#          Name : Eddy Mwai
#   Date : 23 / 5 / 20
#####################################
#A dictionary is a collection of key value pairs
#syntax:dictionary = ['key':'value']
name = 'john'
colours={'colour':'red'}
vehicle={'type':'toyota', 'plate_number':'KNY316'}
#print(type(colours)) to read the data type : we use the type method

#Accessing elements in a dictionary
print((vehicle['type']), (vehicle['plate_number']))
#example in person
person={'name':'Memz','p_number':'0700381819', 'gender':'male', 'home':'jiji'}
person['colour']='black'
del person['p_number']
print(person['name'])
print(person['gender'])
print(person['home'])
#looping over dictionaries
for key,value in person.items():
    print(f"{key}:{value}")
#print(type(person))
print(person)
#adding

# Initializing dictionaries
student = {"Name":"Memz", "age":24, "sex":"Male"}
print(student["Name"])
print(student["sex"])
print(student["age"])

#adding an item in the dictionary
student["Id_No"] = "21250"
student["club"] = "Mancity"
student["sport"] = "fotball"
print(student)

#starting with an empty dictionary
student1 = {}

#add pairs
student1["fav_food"] = "turkey"
student1["home_city"]="Nairobi"
print(student1)

#modifying values in a dictionary
student["age"] = "18"
print(student["age"])

#removing an element
del student1["fav_food"]
print(student1)