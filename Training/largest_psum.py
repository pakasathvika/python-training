''' ip:
        [4,8,14,22,36,68]
    op:
        4-8: largest prime number: 7
        8-14: 13
        14-22 : 19
        22-36: 31
        36-68: 67
        sum of all largest prime numbers
       sum= 7+13+19+31+67 '''

def isprime(x):
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1

def lprime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0

l=list(map(int,input().split(',')))
s=0
for i in range(len(l)-1):
    s=s+lprime(l[i],l[i+1])
print(s)
