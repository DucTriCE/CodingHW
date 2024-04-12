class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA:ListNode, headB: ListNode):
    curA = headA
    curB = headB
    while curA:
        curA.val = None
        curA = curA.next
    while curB:
        if curB.val==None:
            return curB
        else:
            curB = curB.next
    return None

if __name__ == '__main__':
    # Create nodes
    lst1 = ListNode(1)
    lst1_1 = ListNode(2)
    lst1_2 = ListNode(3)
    lst1.next = lst1_1
    lst1_1.next = lst1_2

    lst2 = ListNode(5)
    lst2_1 = ListNode(6)
    lst2.next = lst2_1
    lst2_1.next = lst1_2

    lst3 = ListNode(7)
    lst1_2.next = lst3
    print(getIntersectionNode(lst1, lst2).val)

