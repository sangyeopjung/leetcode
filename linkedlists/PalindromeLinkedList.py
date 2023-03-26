# https://leetcode.com/problems/palindrome-linked-list/description/
# tags: palindrome, linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        out = ListNode(0, head)
        prev = fast = slow = out
        
        next = head
        while fast and fast.next:
            fast = fast.next.next
            slow = next
            
            next = slow.next
            slow.next = prev
            prev = slow
        
        left = slow if fast else slow.next
        right = next
        
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
