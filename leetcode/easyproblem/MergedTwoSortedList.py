class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(lst1: ListNode, lst2: ListNode):
    lst3 = ListNode()
    cur = lst3
    while lst1 and lst2:
        if lst1.val < lst2.val:
            cur.next = lst1
            lst1 = lst1.next
        else:
            cur.next = lst2
            lst2 = lst2.next
        cur = cur.next
    cur.next = lst1 or lst2
    return lst3.next

if __name__ == '__main__':
    # Create nodes
    lst1 = ListNode(1)
    lst1_1 = ListNode(2)
    lst1_2 = ListNode(4)
    lst1.next = lst1_1
    lst1_1.next = lst1_2

    lst2 = ListNode(1)
    lst2_1 = ListNode(3)
    lst2_2 = ListNode(4)
    lst2.next = lst2_1
    lst2_1.next = lst2_2

    result = mergeTwoLists(lst1, lst2)
    cur = result
    while cur:
        print(cur.val, end=' ')
        cur = cur.next
    # Link nodes
