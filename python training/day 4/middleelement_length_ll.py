#print middle element &find the length is even or odd 
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
    def middle(self):
        s=self.head
        f=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        print()
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
l1=sll()
l2=sll()
l1.head=node(3)
l1.addback(4)
l1.addback(5)
l1.addfront(2)
l1.addfront(1)
l2.head=node(100)
l2.addback(200)
l2.addback(300)
l2.addfront(10)
l2.addfront(40)
l1.display()
print()
l2.display()
l1.middle()
l1.evenodd()