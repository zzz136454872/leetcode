/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include"ctree.h"
#include"ctools.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//#define testMod
#ifdef testMod
void test() 
{

}
#endif

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

#ifndef testMod

int isLeaf(struct TreeNode* root)
{
    if(root==NULL)
        return 0;
    return (root->left==NULL&&root->right==NULL);
}

int sumOfLeftLeaves(struct TreeNode* root){
    if(root==NULL)
        return 0;
    int out=0;
    if(isLeaf(root->left))
        out+=root->left->val;
    else
        out+=sumOfLeftLeaves(root->left);
    out+=sumOfLeftLeaves(root->right);
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct TreeNode* root=getNode(3);
    root->left=getNode(9);
    root->right=getNode(20);
    root->right->left=getNode(15);
    root->right->right=getNode(7);
    travelTree(root,1);
    printf("%d\n",sumOfLeftLeaves(root));
#endif
    return 0;
}
    
