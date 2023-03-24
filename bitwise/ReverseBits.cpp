// https://leetcode.com/problems/reverse-bits/description/
// tags: bitwise operations

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int out = 0;
        for (int i = 0; i < 32; i++)
        {
            out = out << 1;
            out = out | (n & 1);
            n = n >> 1;
        }
        return out;
    }
};
