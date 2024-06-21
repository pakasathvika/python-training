'''
ip:
    
op:
    4
    
    1 1 1 1 1 1 1
    1 2 2 2 2 2 1
    1 2 3 3 3 2 1
    1 2 3 4 3 2 1
    1 2 3 3 3 2 1
    1 2 2 2 2 2 1
    1 1 1 1 1 1 1 " '''

a=int(input())
k=1
for i in range(a):
    for j in range(a):
        if i==0 or j==0 or i==a-1 or j==a-1:
            print("1",end=" ")
        elif i==1 or j==1 or i==a-2 or j==a-2:
            print("2",end=" ")
        elif i==2 or j==2 or i==a-3 or j==a-3:
            print("3",end=" ")
        elif i==3 or j==3 or i==a-4 or j==a-4:
            print("4",end=" ")
    print()
    
        