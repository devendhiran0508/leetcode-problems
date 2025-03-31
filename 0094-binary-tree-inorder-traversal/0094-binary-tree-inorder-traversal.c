/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 void inorder(struct TreeNode* root, int* result, int* returnSize) {
    if (root == NULL) {
        return;
    }
    inorder(root->left, result, returnSize);
    result[*returnSize] = root->val;
    (*returnSize)++;  
    inorder(root->right, result, returnSize);
}
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int* result = (int*)malloc(1000 * sizeof(int));  
    *returnSize = 0;  
    inorder(root, result, returnSize);
    return result;
}