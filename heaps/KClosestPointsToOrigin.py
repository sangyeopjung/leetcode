# https://leetcode.com/problems/k-closest-points-to-origin/description/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            dist = points[i][0]*points[i][0] + points[i][1]*points[i][1]
            if len(heap) < k:
                heappush(heap, (-dist,i))
            else:
                heappushpop(heap, (-dist,i))
        
        return [points[i] for d,i in heap]
