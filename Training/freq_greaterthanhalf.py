''' ip: [4,8,2,4,4,8,4]
    op: 4
    
    ip: [2,1,2,2]
    op: 2
    
    ip:[6,6,6,6,7]
    op:6
    frequency=len(a)//2
    if count>frequency
    print element
    '''

a=[6,6,6,6,7]
c=1
p=a[0]
for i in range(1,len(a)):
    if(a[i]==p):
        c=c+1
    else:
        c=c-1
        if(c==0):
            c=1
            p=a[i]
print(p)
    
    
    
    
    