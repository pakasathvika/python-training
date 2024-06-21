'''10|ob(b)		->  20|ob(c)     ->  30|ob(d)		->40|None
     h			      hn		      hnn
                                t      '''
#sum of nodes  
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
        s=0
        t=head
        while(t!=None):
            s=s+t.data
            t=t.nxt
        print(s)
l1=sll()
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)
head.nxt.nxt.nxt=node(40)

'''print(head.data)
print(head.nxt.data)
print(head.nxt.nxt.data)'''
l1.display()
    