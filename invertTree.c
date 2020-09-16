/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

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

//Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* invertTree(struct TreeNode* root){
    if(root==NULL)
        return NULL;
    struct TreeNode* l=root->left;
    struct TreeNode* r=root->right;
    l=invertTree(l);
    r=invertTree(r);
    root->left=r;
    root->right=l;
    return root;
}

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod

#endif
    return 0;
}
    
