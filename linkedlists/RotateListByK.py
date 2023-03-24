# https://leetcode.com/problems/rotate-list/description/
# tags: linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
            
        tmp = head
        size = 1
        while tmp.next:
            tmp = tmp.next
            size += 1
        tmp.next = head

        k = size - (k % size)
        for _ in range(k):
            tmp = tmp.next
        head = tmp.next
        tmp.next = None

        return head