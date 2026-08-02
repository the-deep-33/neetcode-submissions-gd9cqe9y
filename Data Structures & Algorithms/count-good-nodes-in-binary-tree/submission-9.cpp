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
    int sumTheNodes(TreeNode* root, int current_max = -101)
    {
        if(!root)
        {
            return 0;
        }
        if(root->val >= current_max)
        {
            current_max = root->val;
            return 1+sumTheNodes(root->left, current_max)+sumTheNodes(root->right, current_max);
        }
        else{
            return sumTheNodes(root->left, current_max)+sumTheNodes(root->right, current_max);
        }
    }
    int goodNodes(TreeNode* root) {
        return sumTheNodes(root);
    }
};
