'''(300/7)-(400/7)

c=0
for i in range(300,400):
    if i%7==0:
        c=c+1
    print(i)
print(c)

f=0
n=int(input())
for i in range(2,int(n/2)):
    if n%i==0:
        f=1
        break
if(f==1):
    
    while(True):
        n=n+1
        f=0
        for i in range(2,int(n/2)):
            if n%i==0:
                f=1
                break
        if(f==0):
            print(n)
            break

else:
    print(" prime")'''

n=7854112
c=0
while(n):
    if(n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)


