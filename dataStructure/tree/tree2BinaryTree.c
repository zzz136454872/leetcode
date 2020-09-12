#include<stdio.h>
#include<stdlib.h>

typedef struct n{
    int val,sonLen;
    struct n *l, *r;
    struct n* son[3];
}node;
// son should be used from index 0

node* getNode(int val)
{
    node* out=(node*)malloc(sizeof(node));
    out->val=val;
    out->l=NULL;
    out->r=NULL;
    for(int i=0;i<3;i++)
        out->son[i]=NULL;
    out->sonLen=0;
    return out;
}

void travelTree(node* root)
{
    if(root==NULL)
        return;
    root->l=NULL;
    root->r=NULL;
    printf("%d ",root->val);
    for(int i=0;i<root->sonLen;i++)
        travelTree(root->son[i]);
}

void travelBinaryTree(node* root)
{
    if(root==NULL)
        return;
    printf("%d ",root->val);
    for(int i=0;i<root->sonLen;i++)
        root->son[i]=NULL;
    root->sonLen=0;
    travelBinaryTree(root->l);
    travelBinaryTree(root->r);
}

node* tree2BinaryTree(node* root)
{
    if(root==NULL||root->son[0]==NULL)
        return root;
    root->l=root->son[0];
    node* tmp=root->son[0];
    tree2BinaryTree(tmp);
    for(int i=1;i<root->sonLen;i++)
    {
        tmp->r=root->son[i];
        tmp=tmp->r;
        tree2BinaryTree(tmp);
    }
    return root;
}

node* binaryTree2Tree(node* root)
{
    if(root==NULL||root->l==NULL)
        return root;
    root->son[0]=root->l;
    root->sonLen=1;
    node* tmp=root->l;
    binaryTree2Tree(tmp);
    tmp=tmp->r;
    while(tmp!=NULL)
    {
        binaryTree2Tree(tmp);
        root->son[root->sonLen++]=tmp;
        tmp=tmp->r;
    }
    return root;
}

int main()
{
    node* root=getNode(7);
    root->son[0]=getNode(8);
    root->sonLen=1;
    root->son[0]->son[0]=getNode(9);
    root->son[0]->son[1]=getNode(10);
    root->son[0]->sonLen=2;
    travelTree(root);
    putchar('\n');
    root=tree2BinaryTree(root);
    travelBinaryTree(root);
    putchar('\n');
    root=binaryTree2Tree(root);
    travelTree(root);
    putchar('\n');
    return 0;
}

