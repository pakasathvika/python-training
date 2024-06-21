''' search an element in a tree '''
''' searching an element in a tree
    and find the depth of the element if found or depth of a perticular node  '''
class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root is None:
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

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')
            
            
    def search(self,root,key):
        if root==None:
            return "not found"
        if root.data == key:
            return "found"
        if root.data < key:
            return self.search(root.right, key)
        return self.search(root.left, key)
    
    
    def depth(self,root,y,c):
        if root==None:
            return -1
        if root.data==y:
            return c
        if root.data>y:
            return self.depth(root.left,y,c+1)
        return self.depth(root.right,y,c+1)
                

# Usage
t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.create(t1.root, 5)
t1.create(t1.root, 15)
t1.create(t1.root, 2)
t1.create(t1.root, 7)
t1.create(t1.root, 1)
t1.create(t1.root, 3)
print(t1.search(t1.root,3))
print(t1.depth(t1.root,3,0))