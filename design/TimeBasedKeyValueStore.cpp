// https://leetcode.com/problems/time-based-key-value-store/description/
// tags: design, hashmap, binary search

class TimeMap {
    unordered_map<string, vector<pair<int, string>>> m;

public:
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        m[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        // case: doesn't exist or before 1st elem
        if (m.find(key) == m.end() || timestamp < m[key][0].first)
        {
            return "";
        }

        // case: after last elem
        if (m[key].back().first <= timestamp)
        {
            return m[key].back().second;
        }

        // case: somewhere in between
        int l = 0;
        int r = m[key].size();
        while (l < r)
        {
            int mid = l + (r-l)/2;
            if (m[key][mid].first < timestamp)
            {
                l = mid + 1;
            }
            else
            {
                r = mid;
            }
        }
        
        return m[key][l].first == timestamp ? m[key][l].second : m[key][l-1].second;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */