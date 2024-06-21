''' all posible paths '''
def fun(i,l):
    l.append(i)
    if(i==2):
        print(l)
        l.pop()
        return 
    for i in d[i]:
        if(i not in l):
            fun(i,l)
    l.pop()
d={5:[7,3],7:[5,4,3],4:[7,8,2],3:[5,7,8],8:[3,4,2],2:[4,8]}
l=[]
fun(5,l)
print(l)



