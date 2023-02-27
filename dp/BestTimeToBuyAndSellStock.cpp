// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
// tags: dp

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int out = 0;
        int curmin = 10000;
        for (int price: prices)
        {
            curmin = min(curmin, price);
            out = max(out, price - curmin);
        }
        return out;
    }
};