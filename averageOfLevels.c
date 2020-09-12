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
    int bufferSize=2;
    int *tmp=(int*)calloc(bufferSize, sizeof(int));
    print_int_star(tmp,bufferSize);
    for(int i=0;i<bufferSize;i++)
        tmp[i]=i+1;
    print_int_star(tmp,bufferSize);
    printf("size: %I64d\n", _msize(tmp));
    bufferSize*=2;
    tmp=(int*)realloc(tmp,bufferSize*sizeof(int));
    printf("size: %I64d\n", _msize(tmp));
    print_int_star(tmp,bufferSize);
    free(tmp);
}
#endif

#ifndef testMod
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* getNode(int val)
{
    struct TreeNode* out=(struct TreeNode*)malloc(sizeof(struct TreeNode));
    out->val=val;
    out->left=NULL;
    out->right=NULL;
    return out;
}

double *out;
int levels=0;
int *count;
int bufferSize=1;

void search(struct TreeNode* root, int level)
{
    if(root==NULL)
        return;
    if(level==levels)
        levels+=1;
    if(level==bufferSize)
    {
        bufferSize*=2;
        out=(double*)realloc(out,sizeof(double)*bufferSize);
        count=(int*)realloc(count,sizeof(int)*bufferSize);
        for(int i=bufferSize/2;i<bufferSize;i++)
        {
            count[i]=0;
            out[i]=0;
        }
    }
    out[level]+=root->val;
    count[level]++;
    search(root->left,level+1);
    search(root->right, level+1);
}

//Note: The returned array must be malloced, assume caller calls free().
double* averageOfLevels(struct TreeNode* root, int* returnSize){
    levels=0;
    //out=(double*)calloc(bufferSize, sizeof(double));
    //count=(int*)calloc(bufferSize, sizeof(int));
    out=(double*)malloc(bufferSize*sizeof(double));
    count=(int*)malloc(bufferSize*sizeof(int));
    memset(out, 0, bufferSize*sizeof(double));
    memset(count, 0, bufferSize*sizeof(int));
    search(root, 0);
    for(int i=0;i<levels;i++)
        out[i]/=count[i];
    *returnSize=levels;
    return out;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct TreeNode* root=getNode(5);
    root->left=getNode(2);
    root->right=getNode(-3);
    //root->right->left=getNode(15);
    //root->right->right=getNode(7);
    int outSize;
    double* out=averageOfLevels(root, &outSize);
    print_double_star(out, outSize);
#endif
    return 0;
}
    
