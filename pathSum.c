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
int bufferSize;
int outSize;
int **out;
int *rcs;
int *stack;
int stackSize;
int stackLoc;

void travel(struct TreeNode* root, int target)
{
    if(root==NULL)
        return;
    if(stackLoc==stackSize)
    {
        stackSize*=2;
        stack=(int*)realloc(stack,sizeof(int)*stackSize);
    }
    stack[stackLoc++]=root->val;
    if(root->left==NULL&&root->right==NULL)
    {
        if(root->val==target)
        {
            if(bufferSize==outSize)
            {
                bufferSize*=2;
                out=(int**)realloc(out,sizeof(int*)*bufferSize);
                rcs=(int*)realloc(rcs,sizeof(int*)*bufferSize);
            }
            out[outSize]=(int*)malloc(sizeof(int)*stackLoc);
            memcpy(out[outSize],stack,sizeof(int)*stackLoc);
            rcs[outSize]=stackLoc;
            outSize++;
        }
    }
    else
    {
        if(root->left!=NULL)
            travel(root->left,target-root->val);
        if(root->right!=NULL)
            travel(root->right,target-root->val);
    }
    stackLoc--;
}

int** pathSum(struct TreeNode* root, int sum, int* returnSize, int** returnColumnSizes){
    bufferSize=2;
    outSize=0;
    out=(int**)malloc(sizeof(int*)*bufferSize);
    rcs=(int*)malloc(sizeof(int)*bufferSize);
    stackSize=2;
    stackLoc=0;
    stack=(int*)malloc(sizeof(int)*stackSize);
    travel(root,sum);
    *returnSize=outSize;
    *returnColumnSizes=rcs;
    free(stack);
    return out;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct TreeNode* root=getTreeNode(5);
    root->left=getTreeNode(4);
    root->left->left=getTreeNode(11);
    root->left->left->left=getTreeNode(7);
    root->left->left->right=getTreeNode(2);
    root->right=getTreeNode(8);
    root->right->left=getTreeNode(13);
    root->right->right=getTreeNode(4);
    root->right->right->left=getTreeNode(5);
    root->right->right->right=getTreeNode(1);
    int outSize;
    int* rcs;
    int sum=22;
    int** out=pathSum(root,sum,&outSize,&rcs);
    print_int_star(rcs,outSize);
    print_int_2star(out, outSize, 4); 
#endif
    return 0;
}
    
