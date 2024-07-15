class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    # return lst == lst[::-1]
    for i in range(len(lst)):
        if lst[i]!=lst[len(lst)-i-1]:
            return False
    return True



if __name__ == '__main__':
    lst1 = ListNode(1)
    lst1_1 = ListNode(2)
    lst1_2 = ListNode(2)
    lst1_3 = ListNode(1)

    lst1.next = lst1_1
    lst1_1.next = lst1_2
    lst1_2.next = lst1_3

    print(isPalindrome(lst1))

        