''' ip :
         [1,2,3,4,1,2,3,1,2]
    op:
        [[1 2 3 4],[1 2 3],[1 2]]
    ip :
        [2,3,1,3,4,3,2]
    op :
        [[2 3 1 4],[3,2],[3]]
    ip:
        [4,5,2,1]
    op :
        [[4 5 2 1]]'''

a=[2,3,1,3,4,3,2]
m=[]
c=0
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if(not str(a[i]).isalpha()):
            if(a[i] not in r):
                c=c+1
                r.append(a[i])
                a[i]='a'
    m.append(r)
print(m)

'''a=[2,3,1,3,4,3,2]
d={}
m=[]
c=0
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
while(c!=len(a)):
    r=[]
    for i in d:
        if(d[i]!=0):
            d[i]=d[i-1]
            c=c+1
            r.append(i)
    m.append(r)
print(m)'''