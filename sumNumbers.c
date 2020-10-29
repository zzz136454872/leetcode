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
int total;
void travelSum(struct TreeNode* now_root, int now_number)
{
    now_number=now_number*10+now_root->val;
    if(now_root->left==NULL&&now_root->right==NULL)
    {
        total+=now_number;
        return;
    }
    if(now_root->left!=NULL)
        travelSum(now_root->left,now_number);
    if(now_root->right!=NULL)
        travelSum(now_root->right,now_number);
}

int sumNumbers(struct TreeNode* root){
    if(root==NULL)
        return 0;
    total=0;
    travelSum(root,0);
    return total;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct TreeNode* root=getTreeNode(1);
    root->left=getTreeNode(2);
    root->right=getTreeNode(3);
    printf("%d\n",sumNumbers(root));
#endif
    return 0;
}
    
