'''sum=0
n=int(input())
while(n>0):
    r=n%10
    sum=sum+r
    n=n//10
print(sum)
count=0
if sum<=9:
    c=0
    for i in range(2,(sum//2)+1):
        if sum%i==0:
            c=1
            break
    if(c==0):
        print("prime")
    else:
        print("not a prime")
elif sum>9:
    c=0
    for i in range(2,(sum//2)+1):
        if sum%i==0:
            c=1
            break
    if(c==0):
        print("prime")
    else:
        print("not a prime")'''

def add(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s
def pnp(x):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1
n=int(input())
m=n
if(n<10):
    print(pnp(n))
else:
    while(1):
        n=add(n)
        break
    print(pnp(n))




    
        
            
            
            
        
            
            
        

    

    
    
    
    
    
    
