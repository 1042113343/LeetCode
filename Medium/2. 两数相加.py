# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        Init = ListNode(0)
        T = Init
        c = 0
        while(l1 is not None or l2 is not None):
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            total = c + x + y
            c = int(total / 10)
            T.next = ListNode(total%10)
            T = T.next
            if l1 is not None: 
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if c > 0:
            T.next = ListNode(c)
        return Init.next
        
