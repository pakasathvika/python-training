''' ip:
        [3,5,9,6,8,10]
        
        sunrise-on how many buildings will sun light fall
        sunset-on how many buildings will sun light fall
        from left -sunsire
        from right -sunset
        
    op:
        4  '''
arr=[3,5,9,6,8,10]
count=0
c=0
l=[0]*len(arr)
r=[0]*len(arr)
m=0
for i in range(len(arr)):
    if(arr[i]>m):
        m=arr[i]
        c=c+1
    l[i]=m
m1=0
for i in range(len(arr)-1,-1,-1):
    if(arr[i]>m1):
        m1=arr[i]
        count=count+1
    r[i]=m1

print(c,count)
