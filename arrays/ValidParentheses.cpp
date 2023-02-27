// https://leetcode.com/problems/valid-parentheses/
// tags: stack

class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> m {
            {'(', ')'}, 
            {'[', ']'}, 
            {'{', '}'}
        };

        stack<char> st;
        for (char c : s)
        {
            if (m.find(c) != m.end())
            {
                st.push(c);
            }
            else
            {
                if (!st.empty() && c == m[st.top()])
                {
                    st.pop();
                }
                else
                {
                    return false;
                }
            }
        }

        return st.empty();
    }
};
