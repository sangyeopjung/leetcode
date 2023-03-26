# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
# tags: heap

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(n[0], i, 1) for i, n in enumerate(nums)] # min heap
        heapify(heap)
        curmax = max(n[0] for n in heap)
        out = [heap[0][0], curmax]

        while True:
            n, i, j = heappop(heap)
            if j == len(nums[i]):
                return out

            curmax = max(curmax, nums[i][j])
            heappush(heap, (nums[i][j], i, j+1))
            if out[1] - out[0] > curmax - heap[0][0]:
                out[0], out[1] = heap[0][0], curmax
