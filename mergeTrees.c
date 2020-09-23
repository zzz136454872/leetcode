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
struct TreeNode* mergeTrees(struct TreeNode* t1, struct TreeNode* t2){
    if(t1==NULL&&t2==NULL)
        return NULL;
    if(t1==NULL)
        return t2;
    if(t2==NULL)
        return t1;
    t1->val+=t2->val;
    t1->left=mergeTrees(t1->left,t2->left);
    t1->right=mergeTrees(t1->right,t2->right);
    return t1;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod

#endif
    return 0;
}
    
