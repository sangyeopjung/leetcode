# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# tags: linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        out = ListNode(0, head)

        fast = head
        for i in range(n):
            fast = fast.next
        
        slow = out
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return out.next