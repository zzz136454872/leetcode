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
//
typedef struct n{
    int val;
    int count;
} node;

node* buffer;
int loc;
int bufferSize;

void dfs(struct TreeNode* root)
{
    if(root==NULL)
        return;
    dfs(root->left);
    if(loc==-1||buffer[loc].val!=root->val)
    {
        loc++;
        if(loc==bufferSize)
        {
            bufferSize*=2;
            buffer=(node*)realloc(buffer,bufferSize*sizeof(node));
        }
        buffer[loc].val=root->val;
        buffer[loc].count=0;
    }
    buffer[loc].count++;
    dfs(root->right);
}

int* findMode(struct TreeNode* root, int* returnSize){
    if(root==NULL)
    {
        *returnSize=0;
        return 0;
    }
    bufferSize=2;
    buffer=(node*)malloc(sizeof(node)*bufferSize);
    loc=-1;
    dfs(root);
    int maxCount=0;
    int maxTimes=0;
    for(int i=0;i<loc+1;i++)
    {
        if(buffer[i].count>maxCount)
        {
            maxCount=buffer[i].count;
            maxTimes=1;
        }
        else if(maxCount==buffer[i].count)
            maxTimes++;
    }
    int *out=(int*)malloc(sizeof(int)*maxTimes);
    int j=0;
    for(int i=0;i<loc+1;i++)
    {
        if(maxCount==buffer[i].count)
            out[j++]=buffer[i].val;
    }
    *returnSize=maxTimes;
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
    root->right->right=getTreeNode(2);
    int outCount;
    int* out=findMode(root,&outCount);
    printf("%d total\n",outCount);
    print_int_star(out,outCount);
#endif
    return 0;
}
    
