// https://leetcode.com/problems/minimum-window-substring/description/
// tags: sliding window

class Solution {
public:
    string minWindow(string s, string t)
    {
        if (s.size() < t.size())
        {
            return "";
        }

        unordered_map<char, int> tmap, smap;
        for (auto c: t)
        {
            tmap[c]++;
        }

        // save results
        int start = -1;
        int minlen = s.length()+1;

        // window contains t when these are equal
        int window_valid_chars = 0;
        int unique_chars = tmap.size();

        int l = 0;
        for (int r = 0; r < s.length(); r++)
        {
            smap[s[r]]++;
            if (tmap.find(s[r]) != tmap.end() && smap[s[r]] == tmap[s[r]])
            {
                window_valid_chars++;
            }
            
            while (window_valid_chars == unique_chars)
            {
                if (r-l+1 < minlen)
                {
                    start = l;
                    minlen = r-l+1;
                }

                smap[s[l]]--;
                if (smap.find(s[l]) != smap.end() && smap[s[l]] < tmap[s[l]])
                {
                    window_valid_chars--;
                }
                l++;
            }
        }
        return start == -1 ? "" : s.substr(start, minlen);
    }
};