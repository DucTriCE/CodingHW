class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def Postorder(root):
    ans = []
    def printPostorder(root):
        if root:
            printPostorder(root.left)
            printPostorder(root.right)
            ans.append(root.val)
    printPostorder(root)
    return ans

# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    lst = Postorder(root)
    print(f"Preorder traversal of binary tree is {lst}")
