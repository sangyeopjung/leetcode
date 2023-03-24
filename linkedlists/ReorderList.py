# https://leetcode.com/problems/reorder-list/description/
# tags: linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        out = ListNode(0, head)

        # find middle
        fast = slow = out
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse everything from middle
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # join
        curr = out
        while prev:
            curr.next = head
            curr = curr.next
            head = head.next

            curr.next = prev
            curr = curr.next
            prev = prev.next
        
        if head: # odd length
            curr.next = head
        
        return out.next
