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

int sum;

void sumGreater(struct TreeNode* root)
{
    if(root==NULL)
        return ;
    sumGreater(root->right);
    sum+=root->val;
    root->val=sum;
    sumGreater(root->left);
}

struct TreeNode* convertBST(struct TreeNode* root){
    sum=0;
    sumGreater(root);
    return root;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct TreeNode* root=getTreeNode(5);
    root->left=getTreeNode(2);
    root->right=getTreeNode(13);
    root=convertBST(root);
    travelTree(root,1);
#endif
    return 0;
}
    
