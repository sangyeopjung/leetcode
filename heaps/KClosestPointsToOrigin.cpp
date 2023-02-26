// https://leetcode.com/problems/k-closest-points-to-origin/

// Max-heap : O(klogn)
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k)
    {
        priority_queue<pair<int, int>> heap; // max heap
        for (int i = 0; i < points.size(); i++)
        {
            int distance = points[i][0]*points[i][0] + points[i][1]*points[i][1];
            if (heap.size() < k)
            {
                heap.push({distance, i});
            }
            else if (distance < heap.top().first)
            {
                heap.pop();
                heap.push({distance, i});
            }
        }

        vector<vector<int>> out;
        while(!heap.empty())
        {
            out.emplace_back(points[heap.top().second]);
            heap.pop();
        }
        return out;
    }
};


// Quickselect : O(n)
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k)
    {
        int start = 0;
        int end = points.size();
        while (true)
        {
            int pivot = partition(points, start, end);
            if (pivot == k-1)
            {
                return vector<vector<int>>(points.begin(), points.begin() + k);
            }
            else if (pivot < k-1)
            {
                start = pivot + 1;
            }
            else
            {
                end = pivot;
            }
        }
    }

    int partition(vector<vector<int>>& points, int start, int end)
    {
        int pivot = start + (end - start) / 2;
        int pivotdist = points[pivot][0]*points[pivot][0]+points[pivot][1]*points[pivot][1];
        swap(points[pivot], points[end-1]);
        for (int i = start; i < end-1; i++)
        {
            if (points[i][0]*points[i][0]+points[i][1]*points[i][1] < pivotdist)
            {
                swap(points[start], points[i]);
                start++;
            }
        }
        swap(points[end-1], points[start]);
        return start;
    }
}