# https://leetcode.com/problems/add-two-numbers/description/
# tags: linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode(0)

        curr = out
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            curr.next = ListNode(val1 + val2 + carry)
            carry = 0
            if curr.next.val >= 10:
                curr.next.val -= 10
                carry = 1
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        return out.next