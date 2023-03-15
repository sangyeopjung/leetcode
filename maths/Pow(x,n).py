# https://leetcode.com/problems/powx-n/
# tags: maths, recursion

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 2:
            return x*x
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(self.myPow(x, n//2), 2)
