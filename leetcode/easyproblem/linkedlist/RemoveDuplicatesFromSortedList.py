class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode):
    st = set()
    tmp = ListNode()
    cur = tmp

    while head != None:
        if head.val not in st:
            st.add(head.val)
            cur.next=head
            head=head.next
            cur=cur.next
        else:
            head=head.next
    cur.next = None
    return tmp.next
    # nodup_list = ListNode(-101)
    # curN = nodup_list
    # while head:
    #     while head.val == curN.val:
    #         if head.next is not None:
    #             head = head.next
    #         else:
    #             curN.next = None
    #             return nodup_list.next
    #     curN.next = head
    #     curN = curN.next
    # return nodup_list.next


if __name__ == '__main__':
    # Create nodes
    lst1 = ListNode(1)
    lst1_1 = ListNode(1)
    lst1_2 = ListNode(2)
    lst1_3 = ListNode(2)
    lst1_4 = ListNode(4)
    lst1_5 = ListNode(4)

    lst1.next = lst1_1
    lst1_1.next = lst1_2
    lst1_2.next = lst1_3
    lst1_3.next = lst1_4
    lst1_4.next = lst1_5
    lst1_5.next = None

    result = deleteDuplicates(lst1)
    curr = result
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    # Link nodes
