// https://leetcode.com/problems/lru-cache/description/
// tags: design, list, hashmap

class LRUCache {
    unsigned int capacity;
    list<pair<int, int>> lru; // key : value
    unordered_map<int, list<pair<int, int>>::iterator> cache; // key -> iterator

public:
    LRUCache(int capacity) : capacity(capacity) {
    }
    
    int get(int key) {
        if (cache.find(key) == cache.end())
        {
            return -1;
        }

        lru.splice(lru.begin(), lru, cache[key]);
        return cache[key]->second;
    }
    
    void put(int key, int value) {
        if (cache.find(key) == cache.end())
        {
            if (cache.size() == capacity)
            {
                cache.erase(lru.back().first);
                lru.pop_back();
            }
            lru.emplace_front(key, value);
            cache[key] = lru.begin();
        }
        else
        {
            cache[key]->second = value;
            lru.splice(lru.begin(), lru, cache[key]);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */