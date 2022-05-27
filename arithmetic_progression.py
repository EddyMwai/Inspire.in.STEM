#########################
#27/05/22
###########################
#AP
#difference  ,,,, d
#number of terms...n
# first in terms of AP....small a

a=int(input("Enter the first number"))
d=int(input("Enter the common difference"))
n=int(input("Enter the number of terms"))
for i in range(1,n+1):
    n_term=a+(i-1)*d
print(n_term)
sum_n=(n/2)*(2*a +(n-1)*d)
print(sum_n)
