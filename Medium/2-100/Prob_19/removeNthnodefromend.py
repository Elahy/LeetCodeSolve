# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow, i = head, head, 0
        while(i<n):
            fast = fast.next
            i += 1
        if (fast == None):
            return head.next
        while(fast.next):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head