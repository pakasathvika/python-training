''' dijkstra algorithm'''

def dijkstra(x):
    d={5:9999,7:9999,4:9999,3:9999,8:9999,2:9999}
    d[x]=0
    vi=[]
    q=[x]
    while(q):
        m=9999
        for i in q:
            if d[i]<m:
                m=d[i]
                x=i
        for i in g[x]:
            if(i[0] not in vi):
                q.append(i[0])
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
        vi.append(x)
        q.remove(x)
    print(d)
g = {
    5: [(7,2),(3,3)],
    7: [(5,2),(4,7),(3,2)],
    4: [(7,7),(8,1),(2,4)],
    3: [(5,3),(7,2),(8,1)],
    8: [(3,1),(4,1),(2,5)],
    2: [(4,4),(8,5)]
}
dijkstra(5)

    
    
