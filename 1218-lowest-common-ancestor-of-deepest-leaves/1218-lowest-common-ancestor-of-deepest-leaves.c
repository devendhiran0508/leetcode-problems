/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 struct Result
 {
    struct TreeNode *node;
    int depth;
 };
 struct Result helper(struct TreeNode* root, int depth)
 {
    if(root==NULL)
    {
        struct Result res={NULL,depth};
        return res;
    }
    struct Result left=helper(root->left,depth+1);
    struct Result right=helper(root->right,depth+1);

    if(left.depth==right.depth)
    {
        struct Result res={root,left.depth};
        return res;
    }
    else if(left.depth>right.depth)
    {
        return left;
    }
    else
    {
        return right;
    }
 }
struct TreeNode* lcaDeepestLeaves(struct TreeNode* root) {
    return helper(root,0).node;
}