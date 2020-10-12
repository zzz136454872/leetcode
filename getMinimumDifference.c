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

struct TreeNode* pre;
int out;

void gmd(struct TreeNode* root)
{
    if(root==NULL)
        return;
    gmd(root->left);
    if(pre!=NULL)
        out=min(out,abs(root->val-pre->val));
    pre=root;
    gmd(root->right);
}

int getMinimumDifference(struct TreeNode* root){
    pre=NULL;
    out=123456;
    gmd(root);
    return out;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct TreeNode* root=getTreeNode(1);
    root->right=getTreeNode(3);
    root->right->left=getTreeNode(2);
    printf("%d\n",getMinimumDifference(root));
#endif
    return 0;
}
    
