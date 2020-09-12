#include<stdio.h>
#include<stdlib.h>

#define max(a,b) (((a)>(b))?(a):(b))

typedef struct n{
    int val;
    struct n *l, *r;
}node;
// son should be used from index 0

node* getNode(int val)
{
    node* out=(node*)malloc(sizeof(node));
    out->val=val;
    out->l=NULL;
    out->r=NULL;
    return out;
}

int getHeight(node* root)
{
    if(root==NULL)
        return 0;
    return max(getHeight(root->l), getHeight(root->r))+1;
}

node* leftAdjust(node* root)
{
    node* newRoot=root->r;
    node *tmp=newRoot->l;
    newRoot->l=root; 
    root->r=tmp;
    return newRoot;
}

node* rightAdjust(node* root)
{
    node* newRoot=root->l;
    node* tmp=newRoot->r;
    newRoot->r=root;
    root->l=tmp;
    return newRoot;
}

node* adjust(node* root)
{
    if(root==NULL)
        return NULL;
    int balance=getHeight(root->l)-getHeight(root->r);
    if(balance>1)
        root=rightAdjust(root);
    else if(balance<-1)
        root=leftAdjust(root);
    return root;
}

node* insert(node* root, int val)
{
    node* tmp=getNode(val);
    if(root==NULL)
        return tmp;
    if(val<root->val)
        root->l=insert(root->l,val);
    else
        root->r=insert(root->r,val);
    root=adjust(root);
    return root;
}

node* findMin(node* root)
{
    while(root->l!=NULL)
        root=root->l;
    return root;
}

node* delete(node* root, int val)
{
    if(root==NULL)
        return NULL;
    if(val<root->val)
    {
        root->l=delete(root->l,val);
        return root;
    }
    if(val>root->val)
    {
        root->r=delete(root->r,val);
        return root;
    }
    if(root->r==NULL)
    {
        node* out=root->l;
        free(root);
        return out;
    }
    node* tmp=findMin(root->r);
    root->val=tmp->val;
    root->r=delete(root->r, tmp->val);
    adjust(root);
    return root;
}

void travelBinaryTree(node* root)
{
    if(root==NULL)
        return;
    travelBinaryTree(root->l);
    printf("%d ",root->val);
    travelBinaryTree(root->r);
}

int main()
{
    node* root=NULL;
    root=insert(root, 4);
    root=insert(root, 2);
    root=insert(root, 1);
    root=insert(root, 7);
    root=insert(root, 3);
    root=insert(root, 6);
    root=insert(root, 5);
    root=delete(root, 4);
    travelBinaryTree(root);
    putchar('\n');
    return 0;
}

