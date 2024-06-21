'''a=[3,8,5,4,3]
   b=[5,0,9,3,2]
   
   op:
   (add even in a,add odd in b)'''
def even(x,sum):
    if(x==len(a)):
        return sum
    if a[x]%2==0:
        sum=sum+a[x]
    t=even(x+1,sum)
    return t
def odd(x,sum):
    if(x==len(b)):
        return sum
    if %2==1:
        sum=sum+b[x]
    t=odd(x+1,sum)
    return t
a=[3,8,5,4,3]
b=[5,0,9,3,2]
print(even(0,0),odd(0,0))


        
    
        