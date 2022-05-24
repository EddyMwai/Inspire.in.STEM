
#############################
#           Dictionaries    #
#          Name : Eddy Mwai
#   Date : 23 / 5 / 20
#####################################

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