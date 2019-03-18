# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1, t2 = l1, l2
        v1, v2 = 0, 0
        tmp = ListNode(0)
        Init = tmp
        while(t1 is not None or t2 is not None):
            v1 = t1.val if t1 is not None else v1
            v2 = t2.val if t2 is not None else v2
            if (v1 <= v2 and t1 is not None) or t2 is None:
                tmp.next = t1
                tmp = tmp.next
                t1 = t1.next
            else:
                tmp.next = t2
                tmp = tmp.next
                t2 = t2.next              
        return Init.next
