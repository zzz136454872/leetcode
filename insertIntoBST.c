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
struct TreeNode* insertIntoBST(struct TreeNode* root, int val){
    if(root==NULL)
    {
        root=(struct TreeNode*)malloc(sizeof(struct TreeNode));
        root->left=NULL;
        root->right=NULL;
        root->val=val;
        return root;
    }
    if(root->val>val)
        root->left=insertIntoBST(root->left,val);
    else
        root->right=insertIntoBST(root->right,val);
    return root;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct TreeNode* root=getTreeNode(4);
    root->left=getTreeNode(2);
    root->right=getTreeNode(7);
    root->left->left=getTreeNode(1);
    root->left->right=getTreeNode(3);
    root=insertIntoBST(root,5);
    travelTree(root,1);

#endif
    return 0;
}
    
