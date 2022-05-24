#learning about Lists
motorcycle_owner = "Moja Jojo"
plate = ['H1234', 'Y1234', 'S1234']
motorcycle = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycle[-1])
#accessing list itemsusing index
#print(motorcycle)
#motorcycle[2]= "Bugatti"#changing element in a list
#print("I love " +str(motorcycle[2]))
#adding elements in a list
motorcycle.append("Bugatti")
motorcycle[2] = 'boxer'
#print(motorcycle)
#task..print all motorcycle with their print numbers
#print(motorcycle[0], (plate[0]))
#print(motorcycle[1], (plate[1]))
#print(motorcycle[2], (plate[2]))
#deleting an item from a list...del
#del motorcycle[0]
#print(motorcycle)
#task print a statement :
#My name is Mojo Jojo and I own a motorcycle plate number
#print("My name is", ( motorcycle_owner ), "and I own a", (motorcycle[1]), "plate", (plate[1]))
#print(f"My name is {motorcycle_owner} and I own a {motorcycle[0]} plate number {plate[0]}")
#removing an item from a list
motorcycle.remove("Honda")
print(motorcycle)