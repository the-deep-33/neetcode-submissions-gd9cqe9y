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

        deque<TreeNode*> q;
        vector<vector<int>> levels;

        if(!root)
        {
            return levels;
        }

        q.push_back(root);

        while(!q.empty())
        {
            vector<int> iter;
            int maks = q.size();
            for(int i = 0; i < maks; ++i)
            {
                
                TreeNode* node = q.front();
                iter.push_back(node->val);
                if(node->left)
                {
                    q.push_back(node->left);
                }
                if(node->right)
                {
                    q.push_back(node->right);
                }
                q.pop_front();
            }
            levels.push_back(iter);
        }
        return levels;
    }
};
