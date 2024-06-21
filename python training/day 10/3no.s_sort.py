''' ip:
        [4,9,8,2,14,3,5,6]
    op:
        4 8 9 2 14 3 5 6
          2 8 9 14 3 5 6
            8 9 14 3 5 6
              3 9 14 5 6
                5 9 14 6
                  6 9 14
                  
        [ 4 2 8 3 5 6 9 14] '''

l=[4,9,8,2,14,3,5,6]
'''for i in range(len(l)-2):
    if(l[i]>l[i+1]):
        t=l[i]
        l[i]=l[i+1]
        l[i+1]=t
        print(l[i])
       # l[i+1],l[i+2]=l[i+2],l[i+1]
for i in range(len(l)-1):
    print(l[i],end=',')'''

for i in range(len(l)-2):
    if(l[i]>l[i+1]):
        t=l[i]
        l[i]=l[i+1]
        l[i+1]=t
    if(l[i+1]>l[i+2]):
        temp=l[i+1]
        l[i+1]=l[i+2]
        l[i+2]=temp
    if(l[i]>l[i+1]):
        te=l[i]
        l[i]=l[i+1]
        l[i+1]=te
for i in range(len(l)):
    print(l[i])

    
        
        
    
