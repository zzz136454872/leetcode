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

#define max(a,b) (((a)>(b))?(a):(b))

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

typedef struct {
    int max;
    int min;
    int maxSum;
    bool isBST;
} node;

int maxSumBST(struct TreeNode* root){
    if(root==NULL)
        return 0;
    return msb(root).maxSum;
}

node msb(struct TreeNode* root)
{
    if(root->left==NULL && root->right==NULL)
        return node(root->val,root->val,root->val,true);
    node out;
    out->isBST=true;
    if(root->left!=NULL)
    {
        node ol=msb(root->left);
        if(!ol.isBST)
            out.isBST=false;
        if(root.val<=ol.max)
            out.isBST=false;
        maxSum
    }
}
// not finished

    return out;
}

int main()
{

    return 0;
}
    
