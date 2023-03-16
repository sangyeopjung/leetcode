// https://leetcode.com/problems/reverse-integer/
// tags: maths

class Solution {
public:
    int reverse(int x)
    {
        int out = 0;
        while (x)
        {
            int n = x % 10;
            // check for overflow
            if (x > 0 && out > (INT_MAX - n) / 10
             || x < 0 && out < (INT_MIN - n) / 10)
            {
                return 0;
            }
            out = out * 10 + n;
            x /= 10;
        }

        return out;
    }
};
