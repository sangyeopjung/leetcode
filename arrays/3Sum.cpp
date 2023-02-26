// https://leetcode.com/problems/3sum/description/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums)
    {
        sort(nums.begin(), nums.end()); // O(nlogn)

        vector<vector<int>> out;
        int i = 0;
        while (i < nums.size()-2) // O(n^2)
        {
            int x = nums[i];
            if (x > 0)
            {
                break;
            }

            int j = i+1;
            int k = nums.size()-1;
            while (j < k)
            {
                int y = nums[j];
                int z = nums[k];
                int sum = x+y+z;
                if (sum < 0)
                {
                    j++;
                }
                else if (sum > 0)
                {
                    k--;
                }
                else // if (sum == 0)
                {
                    out.push_back({x, y, z});
                    while (j < k && y == nums[j])
                    {
                        j++;
                    }
                    while (j < k && z == nums[k])
                    {
                        k--;
                    }
                }
            }
            
            while (i < nums.size()-2 && x == nums[i])
            {
                i++;
            }
        }

        return out;
    }
};