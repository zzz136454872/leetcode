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
typedef struct n{
    int rootPut;
    int whole;
    int subWhole;
} Counter;

Counter count(struct TreeNode* root)
{
    Counter c;
    if(root==NULL)
    {
        c.rootPut=123456;
        c.whole=0;
        c.subWhole=0;
        return c;
    }
    Counter c1=count(root->left);
    Counter c2=count(root->right);
    c.rootPut=1+c1.subWhole+c2.subWhole;
    c.whole=min(c.rootPut,min(c1.rootPut+c2.whole,c1.whole+c2.rootPut));
    c.subWhole=min(c1.whole+c2.whole,c.whole);
    //printf("%d %d %d %d\n",root->val,c.rootPut,c.whole,c.subWhole);
    return c;
}

int minCameraCover(struct TreeNode* root){
    Counter c=count(root);
    return c.whole;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct TreeNode* root=getTreeNode(1);
    root->right=getTreeNode(2);
    root->right->right=getTreeNode(3);
    root->right->right->right=getTreeNode(4);
    root->right->right->right->right=getTreeNode(5);
    root->right->right->right->right->left=getTreeNode(6);
    root->right->right->right->right->right=getTreeNode(7);
    root->right->right->right->right->right->left=getTreeNode(8);
    root->right->right->right->right->right->right=getTreeNode(9);
    printf("%d\n",minCameraCover(root));
#endif
    return 0;
}
    
