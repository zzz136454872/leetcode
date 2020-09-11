#include<stdio.h>
#include<stdlib.h>

typedef struct n{
    int val,ltag,rtag;
    struct n* l,*r;
} node;

//tag = 0 has child 
//tag = 1 no child 

node* getNode(int val)
{
    node* out=(node*)malloc(sizeof(node));
    out->val=val;
    out->ltag=0;
    out->ltag=0;
    out->l=NULL;
    out->r=NULL;
    return out;
}

void printNode(node* root)
{
    printf("%I64x, %d: %d: %d\n",(unsigned long long)root,root->val, root->ltag, root->rtag);
    printf("%I64x, %I64x\n\n", (unsigned long long)root->l, (unsigned long long)root->r);
}

node* pre;

node* createSub(node* root)
{
    if(root==NULL)
        return NULL;
    createSub(root->l);
    if(root->l!=NULL)
        root->ltag=0;
    else
    {
        root->ltag=1;
        root->l=pre;
    }
    if(root->r!=NULL)
        root->rtag=0;
    else
        root->rtag=1;
    if(pre!=NULL)//pre does not have right son, or it is not pre. 
        pre->r=root;
    pre=root;
    createSub(root->r);
    return root;
}

node* createTree(node* root)
{
    pre=NULL;
    createSub(root);
    return root;
}

node* getNext(node* p)
{
    if(p==NULL)
        return NULL;
    if(p->rtag) //no right child
        return p->r;
    p=p->r;
    while(p->ltag==0)
        p=p->l;
    return p;
}

node* getPre(node* p)
{
    if(p==NULL)
        return NULL;
    if(p->ltag)
        return p->l;
    p=p->l;
    while(p->rtag==0)
        p=p->r;
    return p;
}

node* getHead(node* root)
{
    if(root==NULL)
        return NULL;
    while(root->l!=NULL)
        root=root->l;
    return root;
}

node* getTail(node* root)
{
    if(root==NULL)
        return NULL;
    while(root->r!=NULL)
        root=root->r;
    return root;
}

void travel(node* root)
{
    while(root!=NULL)
    {
        printf("%d ", root->val);
        root=getNext(root);
    }
    putchar('\n');
}

void reverseTravel(node* root)
{
    while(root!=NULL)
    {
        printf("%d ", root->val);
        root=getPre(root);
    }
    putchar('\n');
}

int main()
{
    node* root=getNode(1);
    root->l=getNode(2);
    root->r=getNode(3);
    root->l->l=getNode(4);
    root->r->r=getNode(5);
    root->l->l->r=getNode(6);
    root=createTree(root);
    node* tmp;
    reverseTravel(root);
    travel(root);
    tmp=getTail(root);
    reverseTravel(tmp);
    tmp=getHead(root);
    travel(tmp);
    return 0;
}
