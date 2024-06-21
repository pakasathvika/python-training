''' visiting all nodes using bfs'''
def bfs(d,n):
    vi=[]
    q=[n]
    while(q):
        for i in d[q[0]]:
            if(i not in q and i not in vi):
                q.append(i)
        vi.append(q.pop(0))
        print(vi[-1],end=' ')
    
d={5:[7,3],7:[5,4,3],4:[7,8,2],3:[5,7,8,17],8:[3,4,2,9],2:[4,8,6],6:[2,12],12:[6,9],9:[8,12,10],10:[9],17:[3]}
l=[]
bfs(d,5)

    
    