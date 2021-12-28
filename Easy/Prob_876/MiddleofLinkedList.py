# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowHead = head
        fastHead = head
        while fastHead and fastHead.next:
            slowHead = slowHead.next
            fastHead = fastHead.next.next
        return slowHead
        