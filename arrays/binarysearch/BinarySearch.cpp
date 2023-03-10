// https://leetcode.com/problems/binary-search/description/
// tags: binary search

class Solution {
public:
    int search(vector<int>& nums, int target)
    {
        int l = 0;
        int r = nums.size();
        while (l < r)
        {
            int m = l + (r-l)/2;
            if (nums[m] == target)
            {
                return m;
            }
            else if (nums[m] < target)
            {
                l = m+1;
            }
            else
            {
                r = m;
            }
        }

        return -1;
    }
};