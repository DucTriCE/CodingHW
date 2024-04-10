class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def isSameTree1(p, q) -> bool:
#     if p is None and q is None:
#         return True
#     if p and q:
#         return (p.val == q.val) and (isSameTree1(p.left, q.left)) and (isSameTree1(p.right, q.right))
#     return False


def isSameTree(p, q) -> bool:
    if p is None and q is None:
        return True
    if p is not None and q is not None:
        return (p.val==q.val) and (isSameTree(p.left, q.left)) and (isSameTree(p.right, q.right))
    return False

if __name__ == '__main__':
    root1 = Node(1)
    root2 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)

    print(isSameTree(root1, root2))
