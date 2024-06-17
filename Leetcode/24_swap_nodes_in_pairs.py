# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre_head = dummy = ListNode(0)
        dummy.next = head
        first = head
        second = head.next
        while dummy.next and dummy.next.next:

            # Assign
            first = dummy.next
            second = dummy.next.next
            
            # swap
            first.next = second.next
            dummy.next = second
            second.next = first

            # next iteration
            dummy = first
        
        return pre_head.next


