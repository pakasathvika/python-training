def fun(x):
    if(x==3):
        return 500
    print(x)
    t=fun(x+1)
    print(x)
    return t
print(fun(1))

def fun(x,s):
    if(x==len(a)):
        return s
    s=s+a[x]
    return fun(x+1,s)
a=[6,7,2]
print(fun(0,0))