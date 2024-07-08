# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorderTraversal(self, root):
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

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    lst = root.inorderTraversal(root)
    print(lst)