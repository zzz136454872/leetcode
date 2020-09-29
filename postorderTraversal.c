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
int* postorderTraversal(struct TreeNode* root, int* returnSize){
    int bufferSize=2;
    int stackSize=2;
    struct TreeNode** stack1=(struct TreeNode**)malloc(sizeof(struct TreeNode*)*stackSize);
    int *stack2=(int*)malloc(sizeof(int)*stackSize);
    int* out=(int*)malloc(sizeof(int)*bufferSize);
    int stackPointer=0;
    int outPointer=0;
    struct TreeNode* p=root;
    int sign;
    while(p!=NULL||stackPointer>0)
    {
        if(p!=NULL)
        {
            if(stackPointer==stackSize)
            {
                stackSize*=2;
                stack1=(struct TreeNode**)realloc(stack1,sizeof(struct TreeNode*)*stackSize);
                stack2=(int*)realloc(stack2,sizeof(int)*stackSize);
            }
            stack1[stackPointer]=p;
            stack2[stackPointer++]=0;
            p=p->left;
        }
        else //stackPinter > 0
        {
            p=stack1[--stackPointer];
            sign=stack2[stackPointer];
            if(sign==0)
            {
                sign++;
                stack1[stackPointer]=p;
                stack2[stackPointer++]=sign;
                p=p->right;
            }
            else
            {
                if(outPointer==bufferSize)
                {
                    bufferSize*=2;
                    out=(int*)realloc(out,sizeof(int)*bufferSize);
                }
                out[outPointer++]=p->val;
                p=NULL;
            }
        }
    }
    free(stack1);
    free(stack2);
    *returnSize=outPointer;
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
    int outSize;
    int* out=postorderTraversal(root,&outSize);
    print_int_star(out,outSize);

#endif
    return 0;
}
    
