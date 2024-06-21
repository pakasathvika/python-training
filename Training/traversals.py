''' tree ,inorder,preorder,postorder
    sum of all nodes & types of sums '''
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


    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')
    def sum(self,root):
        if(root==None):
            return 0
        return root.data+self.sum(root.left)+self.sum(root.right)          #preorder traversal sum
    def evensum(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        else:
            return self.evensum(root.left)+self.evensum(root.right)
    def oddsum(self,root):
        if(root==None):
            return 0
        if(root.data%2!=0):
            return root.data+self.oddsum(root.left)+self.oddsum(root.right)
        else:
            return self.oddsum(root.left)+self.oddsum(root.right)
    def diff_eosum(self,root):
        es=0
        os=0
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data + self.diff_eosum(root.left) + self.diff_eosum(root.right)
        return self.diff_eosum(root.left) + self.diff_eosum(root.right) - root.data
    #def height(self,root):
     #   if(root==Node):
      #      return -1
       # return max(self.height(root.left),self.height(root.right))+1
       
    '''def height(self, root):
        if root==None:
            return -1
        return max(self.height(root.left), self.height(root.right)) + 1 '''
        
    
    
t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.create(t1.root, 5)
t1.create(t1.root, 15)
t1.create(t1.root, 2)
t1.create(t1.root, 7)
t1.create(t1.root, 1)
t1.create(t1.root, 3)

print("Inorder traversal:")
t1.inorder(t1.root)
print("\nPreorder traversal:")
t1.preorder(t1.root)
print("\nPostorder traversal:")
t1.postorder(t1.root)
print()
print("sum:",t1.sum(t1.root))
print("sum of left sub tree:",t1.sum(t1.root.left))                      # sum of left sub tree
print("diff of left and right sub tree:",t1.sum(t1.root.left)-t1.sum(t1.root.right))
      #diff b/w right sub tree and left sub tree
print("evensum:",t1.evensum(t1.root))
print("oddsum:",t1.oddsum(t1.root))
print("difference of evenodd sum:",abs(t1.diff_eosum(t1.root)))
#print(t1.height(t1.root))
#t1.bal(t1.root)