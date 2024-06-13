# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterate both the list together. 
            Sum up their value. Update the carrym & summ if summ is greater than 10
        
        Append l1 or l2 if one of the numbers is larger than the other. 
        """
        head = suml = ListNode(0) # Start from a dummy node
        carry = 0
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        while l1 and l2:
            summ = l1.val + l2.val + carry
            carry = summ // 10
            summ %= 10 
            suml.next = ListNode(summ)
            suml = suml.next
            l1 = l1.next
            l2 = l2.next
            
        remaining_list = l1 if l1 else l2
        while remaining_list:
            summ = remaining_list.val + carry 
            carry = summ // 10
            summ %= 10
            suml.next = ListNode(summ)
            suml = suml.next
            remaining_list = remaining_list.next
        
        if carry:
            suml.next = ListNode(carry)
            
        
        return head.next
       