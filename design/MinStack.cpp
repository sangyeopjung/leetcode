// https://leetcode.com/problems/min-stack/description/
// tags: stack, design

class MinStack {
public:
    vector<int> st;
    vector<int> minval;

    MinStack() {
    }
    
    void push(int val) {
        st.push_back(val);
        if (minval.empty() || minval.back() >= val)
        {
            minval.push_back(val);
        }
        else
        {
            minval.push_back(minval.back());
        }
    }
    
    void pop() {
        st.pop_back();
        minval.pop_back();
    }
    
    int top() {
        return st.back();
    }
    
    int getMin() {
        return minval.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */