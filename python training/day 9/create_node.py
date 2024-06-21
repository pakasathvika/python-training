'''class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
        
class tree:
    def __init__(self):
        self.root=None
    def creat(self,root,x):
        if(root==None):
            self.root=node(x)
        elif(root.data>x):
            root.left=self.creat(root.left,x)
        else:
            root.right=self.creat(root.right,x)
        return root
    def inorder(self,root):
        if(root):
            self.inorder(root.left)
            print(root.data,end='')
            self.inorder(root.right)
    def preorder(self,root):
        if(root):
            print(root.data,end='')
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end='')
   
        
t1=tree()
t1.root = t1.creat(t1.root, 10)
t1.creat(t1.root,5)
t1.creat(t1.root,20)
t1.creat(t1.root,7)
t1.creat(t1.root,2)
t1.creat(t1.root,1)
t1.inorder(t1.root)
t1.preorder(t1.root)
t1.postorder(t1.root)'''

