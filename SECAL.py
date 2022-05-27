#########################
# SECALDRYCLEANERS
#25/05/22
######################
type_of_cloth=['suit', 'trouser', 'shirt', 'jacket']
clothes = input("You have?" + str(type_of_cloth))
pieces = input("Pieces?")
date_received = input("Date received?") 
name = input("Mr/Mrs/REV..")
if clothes == 'suit':
    amount =450
elif clothes == 'trouser':
    amount = 300 
print(clothes)