/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include"ctools.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"ctree.h"

//#define testMod
#ifdef testMod
void test() 
{

}
#endif

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

#ifndef testMod
// your code here

struct TreeNode* sub(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q)
{
    if(q->val<root->val)
        return sub(root->left, p, q);
    if(p->val>root->val)
        return sub(root->right,p,q);
    return root;
}

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    if(p->val>q->val)
        return sub(root, q, p);
    return sub(root,p,q);
}


#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct TreeNode* root=getTreeNode(6);
    root->left=getTreeNode(2);
    root->right=getTreeNode(8);
    root->left->left=getTreeNode(0);
    root->left->right=getTreeNode(4);
    root->left->right->left=getTreeNode(3);
    root->left->right->right=getTreeNode(5);
    root->right->left=getTreeNode(7);
    root->right->right=getTreeNode(9);
    struct TreeNode *p=root->left;
    struct TreeNode *q=root->right;
    struct TreeNode* out=lowestCommonAncestor(root,p,q);
    printf("%d\n",out->val);
#endif
    return 0;
}
    
