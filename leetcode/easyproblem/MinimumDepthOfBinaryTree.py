class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end=" "),
        printInorder(root.right)

def minDepth(root: TreeNode):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if root.left is None:
        return minDepth(root.right)+1
    elif root.right is None:
        return minDepth(root.left)+1
    return min(minDepth(root.left), minDepth(root.right))+1


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    # root1.left.left = TreeNode(4)
    # root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(5)
    print(minDepth(root1))
