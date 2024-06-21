'''n=int(input())
rev=0
t=n
while(t!=0):
    r=t%10
    rev=(rev*10)+r
    t=t//10
if(rev==n):
    print("palindrome")
else:
    print("not a palindrome")'''
    
def fun(x,re):
    if(x==0):
        return re
    re=re*10+(x%10)
    return fun(x//10,re)
n=int(input())
if(n==fun(n,0)):
    print("pal")
else:
    print("not pal")
        
    

    
