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
int* preorderTraversal(struct TreeNode* root, int* returnSize){
    int bufferSize=2;
    int retBufferSize=2;
    //int* stack1=(int*)malloc(sizeof(int)*bufferSize);
    struct TreeNode** stack=(struct TreeNode**)malloc(sizeof(struct TreeNode*)*bufferSize);
    int stackPointer=0;
    int outSize=0;
    int* out=(int*)malloc(sizeof(int)*retBufferSize);
    stack[stackPointer++]=root;
    struct TreeNode* now;
    while(stackPointer>0)
    {
        now=stack[--stackPointer];
        if(now!=NULL)
        {
            if(outSize==retBufferSize)
            {
                retBufferSize*=2;
                out=(int*)realloc(out,sizeof(int)*retBufferSize);
            }
            out[outSize++]=now->val;
            if(stackPointer>=bufferSize-1)
            {
                bufferSize*=2;
                stack=(struct TreeNode**)realloc(stack,sizeof(struct TreeNode*)*bufferSize);
            }
            stack[stackPointer++]=now->right;
            stack[stackPointer++]=now->left;
        }
    }
    *returnSize=outSize;
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
    struct TreeNode* root=getTreeNode(1);
    root->right=getTreeNode(2);
    root->right->left=getTreeNode(3);
    int retSize;
    int *out=preorderTraversal(root,&retSize);
    print_int_star(out,retSize);
#endif
    return 0;
}
    
