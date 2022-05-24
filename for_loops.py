school =['Joy','Hope','Mercy','Happy']
pupil =['Peace','Patience','Amani','Charity']
#hard way
#print(school[2], pupil[2])
#print(school[3], pupil[3])
#for pupil in pupil:
       # print(f"Hello I am {pupil}")
        #############################
        #loops : for loop
        #name : memz
        # 23/05/22
        ############################
print("number\tsquare")    
print("==============")   
for number in range (0,9):
    print(number, "\t", number**2)
    #######################
row = int(input("enter the number of rows: "))
for i in range(row):
    print("  "*(row-i)+" *"* (i+1))