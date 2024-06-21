#add even nodes&search element
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
l1.addeven()
print(l1.search(4))