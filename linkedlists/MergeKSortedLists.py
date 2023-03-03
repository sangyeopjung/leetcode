# https://leetcode.com/problems/merge-k-sorted-lists/description/
# tags: linked list, mergesort

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        step = 1
        while step < len(lists):
            i = 0
            while i+step < len(lists):
                lists[i] = self.merge2Lists(lists[i], lists[i+step])
                i += step*2
            step *= 2
        return lists[0]

    def merge2Lists(self, l1, l2):
        out = ListNode(0)
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
        
        return out.next