# https://leetcode.com/problems/sort-list/description/
# tags: linked list, merge sort

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        L = 0
        node = head
        while node:
            L += 1
            node = node.next

        return self.mergesort(head, L)
    
    def mergesort(self, node, L):
        if L == 1:
            return node
        if L == 2:
            if node.val > node.next.val:
                node.val, node.next.val = node.next.val, node.val
            return node

        curr = node
        for i in range(L//2 - 1):
            curr = curr.next
        mid = curr.next
        curr.next = None
        
        return self.merge(self.mergesort(node, L//2), self.mergesort(mid, L//2 + L%2))

    def merge(self, l1, l2):
        if l1.val <= l2.val:
            out = l1
            l1 = l1.next
        else:
            out = l2
            l2 = l2.next

        curr = out
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2
        
        return out
