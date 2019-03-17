# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        T = head
        while(T is not None and T.next is not None):
            if T.next.val == T.val:
                T.next = T.next.next
            else:
                T = T.next
        return head
