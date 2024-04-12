class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    curr = head
    while curr:
        if curr.val == None:
            return True
        curr.val = None
        curr = curr.next
    return False

if __name__ == '__main__':
    lst1 = ListNode(1)
    lst1_1 = ListNode(2)
    lst1_2 = ListNode(4)
    lst1_3 = ListNode(5)

    lst1.next = lst1_1
    lst1_1.next = lst1_2
    lst1_2.next = lst1_3
    # lst1_3.next = lst1_1

    print(hasCycle(lst1))

        