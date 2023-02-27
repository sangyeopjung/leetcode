// https://leetcode.com/problems/evaluate-reverse-polish-notation/
// tags: stack

class Solution {
public:
    long evaluate(long a, long b, char oper)
    {
        switch (oper)
        {
            case '+':
                return a+b;
            case '-':
                return a-b;
            case '*':
                return a*b;
            default: // '/'
                return a/b;
        }
    }

    int evalRPN(vector<string>& tokens) {
        unordered_set<string> operators({"+", "-", "*", "/"});
        stack<long> st;
        for (string s : tokens)
        {
            if (operators.find(s) != operators.end())
            {
                long b = st.top(); st.pop();
                long a = st.top(); st.pop();
                st.push(evaluate(a, b, s[0]));
            }
            else
            {
                st.push(stoi(s));
            }
        }
        return st.top();
    }
};
