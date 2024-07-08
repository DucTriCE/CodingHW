# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode):
    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

if __name__ == '__main__':
    val = 2

    lst1 = ListNode(1)
    lst1_1 = ListNode(3)
    lst1_2 = ListNode(5)
    lst1_3 = ListNode(7)
    lst1_4 = ListNode(9)
    lst1.next = lst1_1
    lst1_1.next = lst1_2
    lst1_2.next = lst1_3
    lst1_3.next = lst1_4

    cur =  reverseList(lst1)
    while cur:
        print(cur.val, end=' ')
        cur = cur.next