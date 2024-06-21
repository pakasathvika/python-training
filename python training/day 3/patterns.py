'''
ip:
    5
op:
    * * * * *
    * 1 2 3 *
    * 4 5 6 *
    * 7 8 9 *
    * * * * * '''
a=5
number=1
for i in range(a):
    for j in range(a):
        if i== 0 or j==0 or i == a-1 or j == a-1:
            print('*', end=' ')
        else:
            print(number, end=' ')
            number = number+1
            
    print()


