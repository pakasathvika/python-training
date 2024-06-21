''' ip:
        5 7 8 2 1 4
    op:
        7 5 2 8 4 1 '''
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
    '''def change_ele(self):
        t=self.head
        t1=t.nxt
        t3=None
        while(t!=None):
            t.nxt=t1.nxt
            t1.nxt=t
            t1.prev=t1
            t.prev=t1
            if(t==self.head):
                self.head=t1
            else:
                t3.nxt=t1
            t,t1=t1,t
            t3=t1'''
    '''def addeven(self):
        t=self.head
        s=0
        sum=0
        diff=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            else:
                sum=sum+t.data
            t=t.nxt
        print()
        s-sum
        print(abs(s-sum))'''
    def evenodd(self,t,es,os):
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.evenodd(t.nxt,es,os)
    def countprime(self,t,c):
        if(t==None):
            return c
        def pnt(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return pnt(s+1,n)
        if(pnt(2,t.data)):
            c=c+1
        return self.countprime(t.nxt,c)
            
        
            
            
            
        

l1=dll()
#l1.head=node(110)
#l1.tail=l1.head
l1.addfront(300)
l1.addfront(237)
#l1.addfront(130)
#l1.addfront(300)
l1.addback(132)
l1.addback(125)

l1.display()
#a=l1.evenodd(l1.head,0,0)
#print(a)
print(l1.countprime(l1.head,0))

