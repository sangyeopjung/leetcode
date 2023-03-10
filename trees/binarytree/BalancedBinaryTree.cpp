// https://leetcode.com/problems/balanced-binary-tree/
// tags: bst, dfs

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
    int depth(TreeNode* node)
    {
        if (node == nullptr)
        {
            return 0;
        }

        int left_depth = depth(node->left);
        if (left_depth == -1)
        {
            return -1;
        }

        int right_depth = depth(node->right);
        if (right_depth == -1)
        {
            return -1;
        }

        return abs(left_depth - right_depth) <= 1 ? 1 + max(left_depth, right_depth) : -1;
    }

    bool isBalanced(TreeNode* root) {
        return depth(root) != -1;
    }
};
