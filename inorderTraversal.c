/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void print_int_star(int *list, int len)
{
    for(int i=0;i<len;i++)
        printf("%d ",list[i]);
    putchar('\n');
}

void print_int_2star(int **matrix,int row,int col)
{
    for(int i=0;i<row;i++)
        print_int_star(matrix[i],col);
}

void print_double_star(double *list, int len)
{
    for(int i=0;i<len;i++)
        printf("%.2lf ",list[i]);
    putchar('\n');
}

#define max(a,b) (((a)>(b))?(a):(b))

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

struct TreeNode* getNode(int val)
{
    struct TreeNode* out=(struct TreeNode*)malloc(sizeof(struct TreeNode));
    out->left=NULL;
    out->right=NULL;
    out->val=val;
    return out;
}

int bufferSize;
int size;

int *inOrder(struct TreeNode* root, int* buffer)
{
    if(root==NULL)
        return buffer;
    buffer=inOrder(root->left,buffer);
    if(size==bufferSize)
    {
        bufferSize*=2;
        buffer=(int*)realloc(buffer,bufferSize*sizeof(int));
    }
    buffer[size++]=root->val;
    return inOrder(root->right,buffer);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize)
{
    bufferSize=2;
    size=0;
    int* out=(int*)malloc(bufferSize*sizeof(int));
    out=inOrder(root, out);
    *returnSize=size;
    return out;
}

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct TreeNode* root=getNode(1);
    root->right=getNode(2);
    root->right->left=getNode(3);
    int outSize;
    int *out=inorderTraversal(root, &outSize);
    print_int_star(out, outSize);
#endif
    return 0;
}
    
