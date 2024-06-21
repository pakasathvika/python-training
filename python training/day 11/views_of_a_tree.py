from collections import deque
class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root==None:
            return Node(x)
        elif root.data > x:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root
    
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)
        

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)


    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')
    def leftview(self,root,c,l):
        if root==None:
            return
        if c not in l:
            l.append(c)
            print(root.data)
            print(root.data,c)
            
        self.leftview(root.left,c+1,l)
        self.leftview(root.right,c+1,l)
    def rightview(self,root,c,l):
        if root==None:
            return
        if c not in l:
            l.append(c)
            print(root.data,c)
            
        self.leftview(root.right,c+1,l)
        self.leftview(root.left,c+1,l)
    def topview(self,root):
        if root==None:
            return
        d={}
        q=deque([(root,0)])
        while q:
            node,hd=q.popleft()
            if hd not in d:
                d[hd] = node.data
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))
        for i in sorted(d):
            print(d[i], end=' ')
    
            
t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.create(t1.root, 5)
t1.create(t1.root, 15)
t1.create(t1.root, 2)
t1.create(t1.root, 7)
t1.create(t1.root, 11)
t1.create(t1.root, 8)
t1.create(t1.root, 9)
#t1.create(t1.root, 3)
#t1.create(t1.root, 12)
#t1.create(t1.root, 13)
#t1.create(t1.root, 14)
print()
t1.leftview(t1.root,0,[])
print()
t1.rightview(t1.root,0,[])
t1.topview(t1.root)
#for i in d:
 #   print(d[i])