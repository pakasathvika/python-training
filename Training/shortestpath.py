''' shortest path '''
def fun(d,x,e, c, m, l1):
    l.append(x)
    if x == e:
        if c < m:
            m = c
            l1 = l.copy()
        l.pop()
        return m, l1
    for i in d[x]:
        if i[0] not in l:
            m, l1 = fun(d, i[0], e, c + i[1], m, l1)
    l.pop()
    return m, l1

d = {
    5: [(7,2),(3,3)],
    7: [(5,2),(4,7),(3,2)],
    4: [(7,7),(8,1),(2,4)],
    3: [(5,3),(7,2),(8,1)],
    8: [(3,1),(4,1),(2,5)],
    2: [(4,4),(8,5)]
}

l = []
#m, shortest_path=fun(d,5,2,0, 99999, [])
for i in d.keys():
    print(fun(d,5,2,0, 99999, []))
#print("Shortest path:", shortest_path)
#print("Minimum cost:", m)
