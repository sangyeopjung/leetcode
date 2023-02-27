// https://leetcode.com/problems/climbing-stairs/description/
// tags: dp

class Solution {
public:
    int climbStairs(int n)
    {
        if (n == 1)
        {
            return 1;
        }

        int big = 1;
        int small = 1;
        for (int i = 2; i <= n; i++)
        {
            int tmp = small;
            small = big + small;
            big = tmp;
        }
        return small;
    }
};