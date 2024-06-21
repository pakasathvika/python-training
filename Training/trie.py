'''
    Tries
    ip:
        7
        1 school
        1 world
        1 word
        1 scholar                  1-inset the value
        2 word                     2-search the word
        2 wood                     3-search for the prefix 
        3 sch                      4-for given prefix print all possibilities
    op:
        True
        False
        True '''

class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
        
    def prefix(self,prefix):
        t=self.root
        for i in prefix:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    def prefix_words(self,str):
        def fun(t,s):
            if(t.flag==1):
                print(s)
                
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str:
            if(i in t.d):
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
    def largest_prefix(self,str):
        def fun(t,s):
            if(t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str:
            if i in t.d:
                t=t.d[i]
            else:
                return
        fun(t,s)
t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.search(s))
    if(a=='3'):
        print(t1.prefix(s))
    if(a=='4'):
        t1.prefix_words(s)