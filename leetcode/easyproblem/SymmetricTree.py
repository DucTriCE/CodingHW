class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTreeSymmetric(p: Node, q:Node) -> bool:
    if p is None and q is None:
        return True
    if p is not None and q is not None:
        return (p.val==q.val) and (isSameTreeSymmetric(p.left, q.right)) and (isSameTreeSymmetric(p.right, q.left))
    return False

def isSymmetric(root) -> bool:
    if root.left is None and root.right is None:
        return True
    if root.left and root.right:
        return isSameTreeSymmetric(root.left, root.right)
    return False

if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(2)
    root1.left.left = Node(3)
    root1.left.right = Node(4)
    root1.right.left = Node(3)
    root1.right.right = Node(3)
    print(isSymmetric(root1))