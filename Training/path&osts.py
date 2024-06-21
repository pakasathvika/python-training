''' path and their costs '''
def fun(i,l,cost):
    l.append(i)
    print(f"Path: {l}, Cost: {cost}")
        
    for (nn,nc) in d[i]:
        if nn not in l:
            fun(nn,l,cost+nc)
    l.pop()
d={5:[(7,2),(3,3)],
   7:[(5,2),(4,7),(3,2)],
   4:[(7,7),(8,1),(2,4)],
   3:[(5,3),(7,2),(8,1)],
   8:[(3,1),(4,1),(2,5)],
   2:[(4,4),(8,5)]
   }

l=[]
fun(5,l,0)
print(l)




