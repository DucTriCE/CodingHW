# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)
'''

def checkHeight(root):
    if root is None:
        return 0
    
    lh = checkHeight(root.left)
    if lh == -1:
        return -1
    rh = checkHeight(root.right)
    if rh == -1:
        return -1
    
    if (abs(lh - rh) > 1):
        return -1
    else:
        return max(lh, rh) + 1

def isBalancedII(root):
    return checkHeight(root)!=-1
 


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