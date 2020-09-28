/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include"ctools.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//#define testMod
#ifdef testMod
void test() 
{

}
#endif

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

#ifndef testMod
//Definition for a Node.
struct Node {
    int val;
    struct Node *left;
    struct Node *right;
    struct Node *next;
};

struct Node * getNode(int val)
{
    struct Node* out=(struct Node*)malloc(sizeof(struct Node));
    out->val=val;
    out->left=NULL;
    out->right=NULL;
    out->next=NULL;
    return out;
}

struct Node* connect(struct Node* root) {
    struct Node* head=root;
    struct Node* prev,*nextHead;
    struct Node* now;
    while(head!=NULL)
    {
        now=head;
        prev=NULL;
        nextHead=NULL;
        while(now!=NULL)
        {
            printf("now: %d\n",now->val);
            if(now->left!=NULL)
            {
                if(nextHead==NULL)
                    nextHead=now->left;
                if(prev!=NULL)
                    prev->next=now->left;
                prev=now->left;
            }
            if(now->right!=NULL)
            {
                if(nextHead==NULL)
                    nextHead=now->right;
                if(prev!=NULL)
                    prev->next=now->right;
                prev=now->right;
            }
            now=now->next;
        }
        head=nextHead;
    }
    return root;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct Node* root=getNode(1);
    //root->left=getNode(2);
    root->right=getNode(2);
    //root->left->left=getNode(4);
    //root->left->right=getNode(5);
    //root->right->right=getNode(7);
    //root=connect(root);
    struct Node* tmp=root->right;
    printf("%x\n",tmp->next);
#endif
    return 0;
}
    
