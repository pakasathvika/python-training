''' ip: [3,2,5,4,1,6,8]
    op: 3 2 5, 3 2 4, 3 2 1 ,... all posibilities '''
arr=[3,2,5,4,1,6,8]
a=len(arr)
i=0
j=0
k=0
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            print(arr[i],arr[j],arr[k])

def combinations(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=[3,5,1,6]
k=3
combinations(a,k) 
        





