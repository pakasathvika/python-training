''' ip:
        5
        0 1 0 0 1
        1 0 0 1 1                       1-land
        0 0 0 0 0                       0-water 
        1 0 0 0 0                       largest island
        1 0 0 0 1
    op:
        5   '''

'''def rec(i,j,n,r):
    if r[i][j]==0:
        return
    r[i][j]=0
    if i > 0:
        rec(i-1,j,n,r)
    if j > 0:
        rec(i,j-1,n,r)
    if i<n-1:
        rec(i+1,j,n,r)
    if j<n-1:
        rec(i,j+1,n,r)
r=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
k=0
n=5

for i in range(n):
    for j in range(n):
        if r[i][j]==1:
            k=k+1
            rec(i,j,n,r)
print(k)  '''

def fun(i,j,c):
    if i<0 or j<0 or i>=n or j>=n or a[i][j]==0:
        return c
    a[i][j]=0
    c=c+1
    c=fun(i-1,j,c)
    c=fun(i,j-1,c)
    c=fun(i+1,j,c)
    c=fun(i,j+1,c)
    return c
a=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
co=0
n=5
m=0
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            k=fun(i,j,0)
            if(k>m):
                m=k
            co=co+1
print(co,m)