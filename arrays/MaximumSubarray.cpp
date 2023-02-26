// https://leetcode.com/problems/maximum-subarray/description/

class Solution {
public:
    int maxSubArray(vector<int>& nums) // O(n)
    {
        int out = nums[0];
        int cursum = 0;
        for (int num : nums)
        {
            cursum += num;
            out = max(out, cursum);
            if (cursum < 0)
            {
                cursum = 0;
            }
        }
        return out;
    }
};