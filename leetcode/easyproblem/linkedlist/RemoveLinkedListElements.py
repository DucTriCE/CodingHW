# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int):
    dummy = ListNode(-1)
    dummy.next = head
    cur = dummy
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next
    # new_list = ListNode(-1)
    # curN = new_list
    # while head:
    #     if head.val == val:
    #         head = head.next
    #     else:
    #         curN.next = head
    #         head = head.next
    #         curN = curN.next
    # curN.next = None
    # return new_list.next


if __name__ == '__main__':
    val = 2

    lst1 = ListNode(2)
    lst1_1 = ListNode(2)
    lst1_2 = ListNode(2)
    lst1_3 = ListNode(2)
    lst1_4 = ListNode(2)
    lst1.next = lst1_1
    lst1_1.next = lst1_2
    lst1_2.next = lst1_3
    lst1_3.next = lst1_4

    cur =  removeElements(lst1, val)
    while cur:
        print(cur.val, end=' ')
        cur = cur.next