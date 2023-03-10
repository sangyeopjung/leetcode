// https://leetcode.com/problems/implement-trie-prefix-tree/description/
// tags: trie

class Trie {
private:
    Trie* children[26];
    bool is_end;

public:
    Trie() : children(), is_end(false)
    {}
    
    void insert(string word)
    {
        Trie* current = this;
        for (char c : word)
        {
            if (current->children[c-'a'] == nullptr)
            {
                current->children[c-'a'] = new Trie();
            }
            current = current->children[c-'a'];
        }
        current->is_end = true;
    }
    
    bool search(string word)
    {
        Trie* current = this;
        for (char c : word)
        {
            if (current->children[c-'a'] == nullptr)
            {
                return false;
            }
            current = current->children[c-'a'];
        }
        return current->is_end;
    }
    
    bool startsWith(string prefix)
    {
        Trie* current = this;
        for (char c : prefix)
        {
            if (current->children[c-'a'] == nullptr)
            {
                return false;
            }
            current = current->children[c-'a'];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */