''' ip:
        3
        xyz
        pqr
        abc
        "yraxpazr"
    op:
        yes
    -------------
    ip:
        4
        abcd
        xyze
        pqrw
        stuv
        "cyptdzsayq"
op:
    no
    ---------------'''

n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
f=0
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        print("no")
        f=1
        break
    else:
        m[i].remove(s[i])
if(f==0):
    print("yes")
    
    
 

'''n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
f=0
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        cntinue
    else:
        f=1
        break
if(f==1):
    print("y")
else:
    print("n")
'''        

 