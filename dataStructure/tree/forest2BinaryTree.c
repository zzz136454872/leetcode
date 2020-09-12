#include<stdio.h>
#include<stdlib.h>

typedef struct n{
    int val,sonLen;
    struct n *l, *r;
    struct n* son[3];
}node;
// son should be used from index 0

typedef struct f{
    node *trees[5];
    int count;
} forest;

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

forest *getForest()
{
    forest* f=(forest*)malloc(sizeof(forest));
    f->count=0;
    for(int i=0;i<5;i++)
        f->trees[i]=NULL;
    return f;
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

void travelForest(forest* f)
{
    printf("forest:\n");
    if(f==NULL)
        return;
    for(int i=0;i<f->count;i++)
    {
        printf("trees[%d]: ", i);
        travelTree(f->trees[i]);
    }
    putchar('\n');
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

forest* binaryTree2Forest(node* root)
{
    if(root==NULL)
        return NULL;
    forest* f=getForest();
    node* tmp=root;
    while(tmp!=NULL)
    {
        f->trees[f->count++]=tmp;
        tmp=tmp->r;
    }
    for(int i=0;i<f->count;i++)
        f->trees[i]=binaryTree2Tree(f->trees[i]);
    return f;
}

node* forest2BinaryTree(forest* f)
{
    if(f==NULL||f->count==0)
        return NULL;
    for(int i=0;i<f->count;i++)
    {
        f->trees[i]=tree2BinaryTree(f->trees[i]);
        if(i<f->count-1)
            f->trees[i]->r=f->trees[i+1];
    }
    node* out=f->trees[0];
    free(f);
    return out;
}


int main()
{
    node* root1=getNode(0);
    root1->son[0]=getNode(1);
    root1->son[1]=getNode(2);
    root1->son[2]=getNode(3);
    root1->sonLen=3;

    node* root2=getNode(4);
    root2->son[0]=getNode(5);
    root2->son[1]=getNode(6);
    root2->sonLen=2;
    
    node* root3=getNode(7);
    root3->son[0]=getNode(8);
    root3->son[0]->son[0]=getNode(9);
    root3->son[0]->son[1]=getNode(10);
    root3->sonLen=1;
    root3->son[0]->sonLen=2;

    forest* f= getForest();
    f->count=3;
    f->trees[0]=root1;
    f->trees[1]=root2;
    f->trees[2]=root3;
    
    travelForest(f);
    node* root=forest2BinaryTree(f);
    travelBinaryTree(root);
    putchar('\n');
    f=binaryTree2Forest(root);
    travelForest(f);
    return 0;
}

