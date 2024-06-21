''' ip:
        6
        0 1 1 1 0 1
        0 1 0 1 0 0
        1 0 1 1 0 0
        0 0 0 1 1 1
        1 1 0 0 0 1
        1 1 1 0 1 0
        4 6
    op:
        8 '''

n=int(input())
for i in range(n):
    a=[]
    for j in range(n):
        a.append(input())
    print()

#print(a[i)
a=int(input())
b=int(input())
c=0

def fun(i,j):
    if(i<0 or j>0 or i>=n or j>=n or a[i][j]!=1):
        return
    if(a[i][j]==1):
        a[i][j]=2
    fun(i-1,j)
    fun(i,j-1)
    fun(i+1,j)
    fun(i,j+1)
    return
fun(i,j)
for i in range(n):
    for j in range(n):
        if(a[i][j]==1):
            c=c+1
print(c)


    