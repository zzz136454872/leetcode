#ifndef ctree_h
#define ctree_h

#include<stdio.h>
#include<assert.h>
#include<stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* getTreeNode(int val)
{
    struct TreeNode* out=(struct TreeNode*)malloc(sizeof(struct TreeNode));
    out->val=val;
    out->left=NULL;
    out->right=NULL;
    return out;
}

//order(int) -> order
//    1      -> preorder
//    2      -> midorder
//    3      -> postorder
void travelTree(struct TreeNode* root,int order)
{
    assert(order>0&&order<4);
    if(root==NULL)
        return;
    if(order==1)
        printf("%d\n", root->val);
    travelTree(root->left,order);
    if(order==2)
        printf("%d\n", root->val);
    travelTree(root->right,order);
    if(order==3)
        printf("%d\n", root->val);
}
#endif
