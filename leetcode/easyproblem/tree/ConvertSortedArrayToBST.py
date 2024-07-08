class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end=" "),
        printInorder(root.right)

def sortedArrayToBST(nums):
    if not nums:
        return 

    mid = len(nums)//2
    root = Node(nums[mid])

    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    root = sortedArrayToBST(nums)
    printInorder(root)
