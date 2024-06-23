#functions and recursions

"""def calc_sum(a,b):
    return a+b

sum=calc_sum(5,7)
print(sum)

print(calc_sum(9,8))"""

#factorial of a number using function
"""def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    return fact

calc_fact(5)"""

#usd to inr

"""def convert(usd):  
    inr=usd*83.59
    print(usd, "USD =", inr, "INR")
    return 0

convert(15)"""

#recursion
"""def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)"""

#sum of first n natural numbers
"""def sum(n):
    if (n==0):
        return 0
    else:
        return sum(n-1)+n

print(sum(10))"""

#print list items using recursion
def print_list(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

print_list([1,2,4,3,5,6,7],1)

    
sum(10)