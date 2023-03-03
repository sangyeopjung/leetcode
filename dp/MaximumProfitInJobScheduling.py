# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# tags: dp, interval, binary search

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        L = len(profit)
        if L == 1:
            return profit[0]

        # O(nlogn) - sort by start time
        sortedlist = []
        for i in range(L):
            sortedlist.append((startTime[i], endTime[i], profit[i]))
        sortedlist.sort()

        # O(nlogn) = binary search for each
        # dp[i] = max profit for items i...L
        #       = max( select current, don't select current )
        #       = max( profit + max at time=end, next item)
        #       = max( profit + dp[j] where j=first item after time=end, dp[i+1])
        dp = [0 for _ in range(L)]
        # base case: always select if there is 1 item
        dp[L-1] = sortedlist[L-1][2]
        for i in range(L-2, -1, -1):
            start, end, prof = sortedlist[i]

            # find the first interval which has its start greater than current's end
            l = 0
            r = L
            while l < r:
                m = (l+r)//2
                if sortedlist[m][0] < end:
                    l = m+1
                else:
                    r = m

            dp[i] = max(prof + (dp[l] if l < L else 0),
                        dp[i+1])
                        
        return dp[0]