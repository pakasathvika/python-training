''' ip:
        4
        tued
        fwow
        roer
        drui
        
        word
    op:
        yes '''

def fun(i,j,k,t):
    if(k==len(s)):
        return 1
    if(i<0 or j<0 or i>=n or j>=n or a[i][j]!=s[k]):
        return
    if(a[i][j]==s[k]):
        a[i][j]
    t=fun(i+1,j,k+1)
    t=fun(i-1,j,k+1)
    t=fun(i,j-1,k+1)
    t=fun(i,j+1,k+1)
    return t
for i in range(n):
    for j in range(n):
        if(a[i][j]==s[0]):
            c=fun(i,j,i,o)
            if(c==1):
                print("yes")
                break
if(c==0):
    print("no")