'''addback'''
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
        s=0
        t=head
        while(t!=None):
            print(t.data)
            t=t.nxt
    
        
    def addback(self,x):
        t=head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    
    '''def search(self):
        k=self.node
        
        while(t!=0):
            if k in t:
                print("found")
            else:
                print("not found")'''
l1=sll()
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)
head.nxt.nxt.nxt=node(40)
l1.addback(20)

'''print(head.data)
print(head.nxt.data)
print(head.nxt.nxt.data)'''
l1.display()
#l1.search()
l1.longest_substring()

    