################




a=int(input("The first term is:"))
r=int(input("The common ratio is:"))
n=int(input("the number of termss are:"))
for i in range(1,n+1):
    n_term=a*r**(i-1)
print(n_term)
sum_n=a*(r**n-1)/(r-1)
print(sum_n)
