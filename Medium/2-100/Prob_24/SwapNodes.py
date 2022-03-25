# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(head):
            if not head.next:
                return head
            dummy = head.next.next if head.next.next else None
            prev = head
            head = head.next
            head.next = prev
            prev.next = recur(dummy) if dummy else None
            return head
            
        return recur(head) if head else head
            