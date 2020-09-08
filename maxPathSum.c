/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define max(a,b) (((a)>(b))?(a):(b))

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


//Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *getNode(int a)
{
    struct TreeNode* tmp=(struct TreeNode*) malloc(sizeof(struct TreeNode));
    tmp->val=a;
    tmp->left=NULL;
    tmp->right=NULL;
    return tmp;
}

int sub1(struct TreeNode* root, int* half_max)
{
    if(root==NULL)
    {
        *half_max=0;
        return -123456;
    }
    int left_half_max,right_half_max;
    int left_max=sub1(root->left, &left_half_max);
    int right_max=sub1(root->right, &right_half_max);
    left_half_max=max(left_half_max,0);
    right_half_max=max(right_half_max,0);
    *half_max=max(left_half_max,right_half_max)+root->val;
    int tmp=max(left_max, right_max);
    return max(tmp, left_half_max+right_half_max+root->val);
}

int maxPathSum(struct TreeNode* root){
    int half_max;
    return sub1(root,&half_max);
}

int main()
{
    struct TreeNode *root=getNode(9);
    root->right=getNode(-3);
    root->right->right=getNode(2);
    root->right->right->left=getNode(2);
    root->right->right->left->left=getNode(-6);
    root->right->right->left->right=getNode(-6);
    printf("%d\n", maxPathSum(root));
    return 0;
}
    
