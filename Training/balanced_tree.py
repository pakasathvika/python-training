''' balanced tree or not '''
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
            
    
    def height(self, root):
        if root==None:
            return -1
        return max(self.height(root.left), self.height(root.right)) + 1
    
    def balance(self,root):
        return (abs(self.height(root.left) - self.height(root.right))) <= 1   
    

# Usage
t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.create(t1.root, 5)
t1.create(t1.root, 15)
t1.create(t1.root, 2)
t1.create(t1.root, 7)
t1.create(t1.root, 1)
t1.create(t1.root, 3)

if(t1.balance(t1.root)):
    print("balanced")
else:
    print("not balanced")
