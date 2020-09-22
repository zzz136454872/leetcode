#include<stdio.h>
#include<stdlib.h>
#include"../../ctools.h"
#include<assert.h>

#define RED 0
#define BLACK 1

//TODO 补全红黑树节点的插入操作

//红黑树节点的定义
//为了方便起见添加一个指向根节点的指针
typedef struct n{
    int val;
    int color;
    struct n*left;
    struct n*right;
    struct n*parent;
} RBTNode;

//获取节点
//由于默认插入的节点是red，所以默认的颜色是red
//指针均为NULL
//需要free
RBTNode *getRBTNode(int val)
{
    RBTNode * out=(RBTNode*)malloc(sizeof(RBTNode));
    out->val=val;
    out->color=RED;
    out->left=NULL;
    out->right=NULL;
    out->parent=NULL;
    return out;
}

//给一个节点添加左子节点
//不处理颜色问题
void addLeft(RBTNode* root,int val)
{
    root->left=getRBTNode(val);
    root->left->parent=root;
}

//给一个节点添加右子节点
//不处理颜色问题
void addRight(RBTNode* root,int val)
{
    root->right=getRBTNode(val);
    root->right->parent=root;
}

//左旋操作
//将root的右子节点作为新的root
//不处理颜色问题
//将返回节点的parent设为NULL
RBTNode* leftAdjust(RBTNode* root)
{
    RBTNode* newRoot=root->r;
    RBTNode *tmp=newRoot->l;
    newRoot->l=root; 
    root->parent=newRoot;
    root->r=tmp;
    tmp->parent=root;
    newRoot->parent=NULL;
    return newRoot;
}

//右旋操作
//将root的左子节点作为新的root
//不处理颜色问题
//将返回节点的parent设为NULL
RBTNode* rightAdjust(RBTNode* root)
{
    RBTNode* newRoot=root->l;
    RBTNode* tmp=newRoot->r;
    newRoot->r=root;
    root->parent=newRoot;
    root->l=tmp;
    tmp->parent=root;
    return newRoot;
}

//插入的过程中，所有左子树中的节点小于当前
//节点，右子树中的节点大于等于当前节点
RBTNode* insert(RBTNode* root, int val)
{
    RBTNode* newNode=getRBTNode(val);
    if(root==NULL)
    {
        newNode->color=BLACK;
        return newNode;
    }
    //寻找插入位置
    RBTNode* p=root;
    while(p->left!=NULL||p->right!=NULL)
    {
        if(p->val>val)
        {
            if(p->left!=NULL)
                p=p->left;
            else
                break;
        }
        else
        {
            if(p->right!=NULL)
                p=p->right;
            else
                break;
        }
    }
    if(p->val>val)//插入左子节点
    {
        p->left=newNode;
        newNode->parent=p;
        if(p->color=BLACK)
            return;//不需要调整
    }
    else//插入右子节点
    {
        p->right=newNode;
        newNode->parent=p;
        if(p->color=BLACK)
            return;//不需要调整
    }
    RBTNode* grand=p->parent;
    RBTNode* uncle=grand->left;
    if(uncle==p)
        uncle=grand->right;
    if(uncle==NULL)
        return;
}

//递归判断是否每个叶节点序列中的
//节点是不是到根节点的路径中黑色
//节点的数量相等
void countBlack(RBTNode* root,int nowCount, int* pCounter)
{
    if(*pCounter<0) //已经发现叶节点路径中黑色节点数量不相等
        return;
    if(root->color==BLACK)
        nowCount++;
    if(root->left!=NULL)
        countBlack(root->left,nowCount, pCounter);
    if(root->left!=NULL)
        countBlack(root->right,nowCount,pCounter);
    if(root->left==NULL&&root->right==NULL)//叶节点
    {
        if(*pCounter==0)
            *pCounter=nowCount;
        else if(*pCounter!=nowCount)
            *pCounter=-1;
    }
}

//判断每个分支的黑色节点的
//数量是不是一样
//0表示黑色节点不平衡
//正数表示节点平衡
//bool的定义在ctools.h中
bool blackBalance(RBTNode* root)
{
    if(root==NULL)
        return true;
    int counter=0;
    countBlack(root,0,&counter);
    return counter>=0;
}

//判断红黑树的字函数
//判断所有的红色节点的孩子是不是都是
//黑节点
bool checkRBTSub(RBTNode* root)
{
    if(root==NULL)
        return true;
    if(!checkRBTSub(root->left)||!checkRBTSub(root->right))
        return false;
    if(root->color==RED)
    {
        if(root->left!=NULL&&root->left->color==RED)
            return false;
        if(root->right!=NULL&&root->right->color==RED)
            return false;
    }
    return true;
}

//检查是不是合法的红黑树的函数
//bool 定义在 ctool.h中
bool checkRBT(RBTNode* root)
{
    if(root==NULL)
        return true;
    if(root->color!=BLACK)
        return false;
    if(!blackBalance(root))
    {
        printf("black");
        return false;
    }
    if(!checkRBTSub(root))
    {
        printf("sub");
        return false;
    }
    return true;
}

int main()
{
    RBTNode* root=getRBTNode(1);
    root->color=BLACK;
    addLeft(root,0);
    addRight(root,100);
    addRight(root->right,100);
    root->left->color=BLACK;
    root->right->right->color=BLACK;
    printf("%d\n",checkRBT(root));
    return 0;
}
