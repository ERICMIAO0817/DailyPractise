from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = head
        count = 1
        if count == 1 and n == 1:
            head.next = None
            head.val = None
            return head
        point = h.next
        while h.next:
            count += 1
            h = h.next
            point = point.next
