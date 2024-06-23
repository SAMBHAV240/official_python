#loops

"""num= int(input("enter the number whose table you want to print:- "))
i=1
while i<=10:
    print( (num*i))
    i+=1"""

n=int(input("enter the number whose factorial you want to print:- "))
fact=1
for i in range(1,n+1):
    fact*=i
print("the required factorail is",fact)
