# https://leetcode.com/problems/odd-even-linked-list/description/
# tags: linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(0)
        even = ListNode(0)

        oddprev = odd
        evenprev = even
        node = head
        while node and node.next:
            oddprev.next = node
            evenprev.next = node.next

            oddprev = oddprev.next
            evenprev = evenprev.next
            node = node.next.next
        
        if node:
            oddprev.next = node
            oddprev = oddprev.next
        
        oddprev.next = even.next
        evenprev.next = None

        return odd.next