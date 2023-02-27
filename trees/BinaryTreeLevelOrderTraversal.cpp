// https://leetcode.com/problems/binary-tree-level-order-traversal/description/
// tags: bfs

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> out;
        queue<TreeNode*> q;
        if (nullptr != root)
        {
            q.push(root);
        }

        while (!q.empty())
        {
            vector<int> curr;
            int size = q.size();
            for (int i = 0; i < size; i++)
            {
                TreeNode* node = q.front(); q.pop();
                curr.push_back(node->val);
                if (nullptr != node->left)
                {
                    q.push(node->left);
                }
                if (nullptr != node->right)
                {
                    q.push(node->right);
                }
            }
            out.emplace_back(move(curr));
        }
        return out;
    }
};
