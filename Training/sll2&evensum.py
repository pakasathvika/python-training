'''2 linked lists'''
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        s=0
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            t=node(x)
            t.nxt=self.head
            self.head=t
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            
            t=t.nxt
        print()
        print(s)
    def search(self,x):
        t=self.head
        while(t!=None):
            if(t.data==x):
                return "found"
            t=t.nxt
        return "not found"
    def middle(self):
        s=self.head
        f=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        print(s.data)
        
        '''t=self.head
        c=0
        while(t!=None):
            c=c+1
            t=t.nxt
        c=c//2
        t=self.head
        for i in range(c):
            t=t.nxt
        print(t.data) '''
        
    def evenodd(self):
       
       s=self.head
       f=self.head
       while(f!=None and f.nxt!=None):
           s=s.nxt
           f=f.nxt.nxt
       if(f==None):
           print("even")
       else:
            print("odd")
    def pairs(self):
        t=self.head
        while t!=None:
            t1=t.nxt
            while t1!=None:
                print(t.data,t1.data)
                t1=t1.nxt
            t=t.nxt
    def longestsubstring(self):
        t=self.head
        c=1
        m=1
        while(t.nxt!=None):
            if(t.data==t.nxt.data-1):
                c=c+1
            else:
                if(c>m):
                    m=c
                c=1
        if(c>m):
            m=c
        print(m)
l1=sll()
l2=sll()
l1.head=node(10)
#head.nxt=node(20)
#head.nxt.nxt=node(30)
#head.nxt.nxt.nxt=node(40)
l1.addback(20)
l1.addback(30)
l1.addfront(2)
l1.addfront(1)
l2.head=node(100)
l2.addback(200)
l2.addback(300)
l2.addfront(10)
l2.addfront(40)

'''print(head.data)
print(head.nxt.data)
print(head.nxt.nxt.data)'''
l1.display()
print()
l2.display()
l1.addeven()
l2.addeven()
print(l1.search(10))
l1.middle()
l1.evenodd()
#
l1.pairs()
l1.longestsubstring()