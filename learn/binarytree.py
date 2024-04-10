class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
    def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end=" "),
        printInorder(root.right)

def printPreorder(root):
    if root:
        print(root.val, end=" "),
        printPreorder(root.left)
        printPreorder(root.right)
 
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end=" "),


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("Inorder traversal of binary tree is ", end='')
    printInorder(root)
    print()
    print("Preorder traversal of binary tree is ", end='')
    printPreorder(root)
    print()
    print("Postorder traversal of binary tree is ", end='')
    printPostorder(root)