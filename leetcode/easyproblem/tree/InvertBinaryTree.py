# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def Inorder(self, root):
        lst = []
        def inorder(root):
            if root:
                inorder(root.left)
                lst.append(root.val)
                inorder(root.right)
            else:
                return []
        inorder(root)
        return lst
    
    def Preorder(self, root):
        ans = []
        def printPreorder(root):
            if root:
                ans.append(root.val)
                printPreorder(root.left)
                printPreorder(root.right)
        printPreorder(root)
        return ans
    
    def Postorder(self, root):
        ans = []
        def printPostorder(root):
            if root:
                printPostorder(root.left)
                printPostorder(root.right)
                ans.append(root.val)
        printPostorder(root)
        return ans
    
    def Levelorder(self, root):
        lst = []
        if not root:
            return

        queue = deque([root])
        while queue:
            node = queue.popleft()
            lst.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return lst

def InvertBinaryTree(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    InvertBinaryTree(root.left)
    InvertBinaryTree(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    InvertBinaryTree(root)
    lst = root.Levelorder(root)
    print(lst)