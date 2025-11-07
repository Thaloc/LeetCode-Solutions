# LeetCode's ListNode is assumed
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = l1
        carry = 0
        prev = None

        # add while both present, write into l1
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry, l1.val = divmod(s, 10)
            prev = l1
            l1 = l1.next
            l2 = l2.next

        # attach remaining of l2 to l1 chain to continue in-place
        if l2:
            prev.next = l2
            l1 = l2

        # propagate carry through the rest
        while l1:
            s = l1.val + carry
            carry, l1.val = divmod(s, 10)
            prev = l1
            l1 = l1.next

        # extra node if carry left
        if carry:
            prev.next = ListNode(carry)

        return head