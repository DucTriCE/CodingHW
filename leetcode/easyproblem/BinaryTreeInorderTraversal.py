# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def insert(self, data):
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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