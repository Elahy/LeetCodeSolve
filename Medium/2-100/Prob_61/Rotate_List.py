# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _getLength(self, head):
        l = 0
        current = head
        while(current is not None):
            l += 1
            current = current.next
        return l
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head is None):
            return None
        l = self._getLength(head)
        k %= l
        p1 = head
        p2 = head
        for _ in range(k):
            p2 = p2.next
        while(p2.next is not None):
            p1 = p1.next
            p2 = p2.next
        p2.next = head
        head = p1.next
        p1.next = None
        return head
        