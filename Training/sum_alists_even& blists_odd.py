''' ip:
       a-[ 6,3,2,9,4,7]
        
        
       b=[8,7,5,3,6,9]
    op:
        [13,11,9,15,9,7,11,11,9,7,13]
        
       sum of each elements of even number in the 'a' list and odd number in the 'b' list'''

def fun():
    for i in range(n):
        for j in range(m):
            if(a[i]%2==0 and b[j]%2!=0):
                r.append(a[i]+b[j])
                j=j+1
        i=i+1
    return r
r=[]
a=[6,3,2,9,4,7]
b=[8,7,5,3,6,9]

n=len(a)
m=len(b)
print(fun())

def fun_rec(i,j,n,m,a,b,r):
    if i>=n:
        return r
    if j>=m:
        return fun_rec(i+1,0,n,m,a,b,r)
    if a[i]%2==0 and b[j]%2!=0:
        r.append(a[i]+b[j])
    return fun_rec(i,j+1,n,m,a,b,r)
r=[]
a=[6,3,2,9,4,7]
b=[8,7,5,3,6,9]

n=len(a)
m=len(b)
print(fun_rec(0,0,n,m,a,b,r))
                