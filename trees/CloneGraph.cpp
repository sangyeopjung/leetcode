// https://leetcode.com/problems/clone-graph/description/
// tags: dfs, hashmap

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node)
    {
        if (nullptr == node)
        {
            return nullptr;
        }

        unordered_map<Node*, Node*> mapping; // orig -> clone
        visit(node, mapping);
        return mapping[node];
    }

    void visit(Node* node, unordered_map<Node*, Node*>& mapping)
    {
        mapping[node] = new Node(node->val);
        for (Node* neighbour : node->neighbors)
        {
            if (mapping.find(neighbour) == mapping.end()) // not visited yet
            {
                visit(neighbour, mapping);
            }
            mapping[node]->neighbors.push_back(mapping[neighbour]);
        }
    }
};