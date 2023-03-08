# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# tags: linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = head.next
        next = head.next.next

        head.next.next = head
        head.next = self.swapPairs(next)

        return prev



class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode(0, head)

        prev = out
        curr = head
        while curr and curr.next:
            next = curr.next.next

            prev.next = curr.next
            curr.next.next = curr
            curr.next = next

            prev = curr
            curr = next
        
        return out.next
