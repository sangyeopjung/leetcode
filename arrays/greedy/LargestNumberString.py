# https://leetcode.com/problems/largest-number/
# tags: greedy, string, sorting

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        out = "".join(sorted([str(n) for n in nums],
                      key=cmp_to_key(lambda n1, n2: 1 if n1 + n2 < n2 + n1 else -1))
                ).lstrip('0')
        return out if len(out) else '0'
