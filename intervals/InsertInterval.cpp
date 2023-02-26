// https://leetcode.com/problems/insert-interval/description/

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> out;
        for (auto& interval : intervals)
        {
            if (interval[1] < newInterval[0]) // case 1: before
            {
                out.push_back(interval);
            }
            else if (newInterval[1] < interval[0]) // case 2: after
            {
                out.push_back(newInterval);
                newInterval = interval;
            }
            else // case 3: overlapping; merge
            {
                newInterval[0] = min(interval[0], newInterval[0]);
                newInterval[1] = max(interval[1], newInterval[1]);
            }
        }
        out.push_back(newInterval);
        return out;
    }
};