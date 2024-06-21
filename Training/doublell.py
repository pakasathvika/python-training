#double linkedlist
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
        print()
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=t
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.nxt=self.head
            self.head.prev=t
            self.head=t
            
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
    def search(self,x):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if(t.data==x or t1.data==nxt):
                return "found"
            t=t.nxt
            t1=t1.prev
        if(t.data==x):
            print("found")
        else:
            print("not found")
    def evenodd(self):
        c=0
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            t=t.nxt
            t1=t.prev
        if(t==t1):
            print("odd length")
        else:
            print("even length")
    def palin(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if(t.data!=t1.data):
                return "not palin"
            t=t.nxt
            t1=t1.prev
        return "palin"
    def set(self):
        f=self.head
        slow=self.head
        while(f!=None):
            f=f.nxt.nxt
            slow=slow.nxt
        self.tail.nxt=self.head
        self.head.prev=self.tail
        t1=slow.prev
        t1.nxt=None
        slow.prev=None
        self.head=slow
        self.tail=t1
    
l1=dll()
#l1.head=node(110)
#l1.tail=l1.head
l1.addfront(300)
l1.addfront(120)
l1.addfront(130)
l1.addfront(300)
l1.addback(130)
l1.addback(120)

l1.display()
l1.rev_display()
print(l1.search(300))
l1.evenodd()
print(l1.palin())
l1.set()
l1.display()
