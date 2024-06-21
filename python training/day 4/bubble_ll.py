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
    
    def bubblesort(self):
        temp=self.head
        p=None
        while(temp.nxt!=p):
            f=0
            t=self.head
            while(t.nxt!=p):
                if(t.data>t.nxt.data):
                    f=1
                    t.data,t.nxt.data=t.nxt.data,t.data
                t=t.nxt
            if(f==0):
                break
            p=t
            temp=temp.nxt
            
        #print(t.data)
            
            
            
    
l1=sll()
l2=sll()
l1.head=node(3)
l1.addback(4)
l1.addback(8)
l1.addfront(6)
l1.addfront(1)
l2.head=node(100)
l2.addback(200)
l2.addback(300)
l2.addfront(10)
l2.addfront(40)
l1.display()
print()
l1.bubblesort()
l1.display()

