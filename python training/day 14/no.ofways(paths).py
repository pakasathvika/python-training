''' ip:
        4x3
        no.of possible ways to reach the -1 position(in all 4 angles) and print paths(ways)
        case 2: with obstacle.
    op:
        ----
        ----
        ----
        10      '''

def fun(i,j,c):
    if(i<0 or i>=n or j<0 or j>=m ):
        return c
    if(i==n-1 and j==m-1):
        c=c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c=fun(i-1,j,c)
    if((i,j-1) not in vi):
        c=fun(i,j-1,c)
    if((i+1,j) not in vi):
        c=fun(i+1,j,c)
    if((i,j+1) not in vi):
        c=fun(i,j+1,c)
    vi.pop()
    return c
n=4
m=3
vi=[]
arr=[]
print(fun(0,0,0))
for i,j in vi:
    print(arr[i][i])