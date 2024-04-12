class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val
    leftSum = hasPathSum(root.left, targetSum-root.val)
    rightSum = hasPathSum(root.right, targetSum-root.val)

    return leftSum or rightSum


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    targetSum = 22
    print(hasPathSum(root, targetSum))