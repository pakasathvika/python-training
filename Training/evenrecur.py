'''def fact(x):
    if(x==1):
        return 1
    return x*fact(x-1)

print(fact(5))'''

def even(x):
    if(x==0):
        return 1
    return x+even(x-2)

x=10
if(x%2==0):
    print(even(x))
else:
    print(even(x-1))