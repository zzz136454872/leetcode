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
    RBTNode* newRoot=root->right;
    RBTNode *tmp=newRoot->left;
    newRoot->left=root; 
    root->parent=newRoot;
    root->right=tmp;
    if(tmp!=NULL)
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
    RBTNode* newRoot=root->left;
    RBTNode* tmp=newRoot->right;
    newRoot->right=root;
    root->parent=newRoot;
    root->left=tmp;
    if(tmp!=NULL)
        tmp->parent=root;
    return newRoot;
}

RBTNode* balanceRBT(RBTNode* newNode,RBTNode* root)
{
    RBTNode* parent=newNode->parent;
    if(parent==NULL)
    {
        newNode->color=BLACK;
        return newNode;
    }
    if(parent->color==BLACK)
        return root;//不需要调整
    RBTNode* grand=parent->parent;
    RBTNode* uncle=grand->left;
    RBTNode* greatgrand=grand->parent;
    if(uncle==parent)
        uncle=grand->right;
    if(uncle!=NULL&&uncle->color==RED)
    {
        grand->color=RED;
        uncle->color=BLACK;
        parent->color=BLACK;
        //这里有可能导致根节点为红色
        //将parent作为新的节点进行处理
        return balanceRBT(grand,root);
    }
    else
    {
        if(parent==grand->left)
        {
            if(newNode==parent->right)
            {
                grand->left=leftAdjust(parent);
                grand->left->parent=grand;
                parent=grand->left;
                newNode=parent->left;
            }
            grand=rightAdjust(grand);
            if(greatgrand!=NULL)
            {
                grand->parent=greatgrand;
                if(greatgrand->left==grand->right)
                    greatgrand->left=grand;
                else
                    greatgrand->right=grand;
            }
            grand->right->color=RED;
            grand->color=BLACK;
            if(greatgrand!=NULL)
                return root;
            else
                return grand;
        }
        else
        {
            if(newNode==parent->left)
            {
                grand->right=rightAdjust(parent);
                grand->right->parent=grand;
                parent=grand->right;
                newNode=parent->right;
            }
            grand=leftAdjust(grand);
            if(greatgrand!=NULL)
            {
                grand->parent=greatgrand;
                if(greatgrand->left==grand->left)
                    greatgrand->left=grand;
                else
                    greatgrand->right=grand;
            }
            grand->left->color=RED;
            grand->color=BLACK;
            if(greatgrand!=NULL)
                return root;
            else
                return grand;
        }
    }
    assert(false);//will not go there
    return NULL;
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
        p->left=newNode;
    else//插入右子节点
        p->right=newNode;
    newNode->parent=p;
    return balanceRBT(newNode,root);
}

//删除节点进行平衡的函数
RBTNode* deleteBalance(p,root)
{
    assert(p!=NULL);
    RBTNode *parent=p->parent;
    if(parent==NULL)
        return;
    RBTNode* uncle;
    RBTNode* grand;
    RBTNode* nephewLeft, nephewRight;
    if(parent->left==p) //p是parent的左子节点
    {
        uncle=parent->right;
        if(uncle!=NULL&&uncle->color=RED)
        {
            grand=parent->parent;
            parent->color=RED;
            uncle->color=BLACK;
            parent=leftAdjust(parent);
            if(grand!=NULL)
            {
                parent->parent=grand;
                if(parent->left==grand->left)
                    grand->left=parent;
                else
                    grand->right=parent;
            }
            return deleteBalance(p,root);
        }
        else
        {
            if(uncle!=NULL&&uncle->right->color==RED)
            {
                uncle->color=parent->color;
                parent->color=BLACK;
                nephewRight=uncle->right;
                if(nephewLeft->color!=
                        //TODO add code here
            }
            else if(uncle!=NULL&&uncle->left->color==RED)
            {
            }
            else
            {
            }
        }
    }
    else
    {

    }
}

//查找一个节点的后继节点
RBTNode* findNext(RBTNode* node)
{
    while(node!=NULL&&node->parent->right==node)
        node==node->parent;
    if(node==NULL)
        return NULL;
    node=node->right;
    while(node->left!=NULL)
        node=node->left;
    return node;
}

//查找删除节点的替代节点
RBTNode* findReplace(RBTNode* node)
{
    if(node->left==NULL&&node->right==NULL)
        return node;
    if(node->left==NULL)
        return findReplace(node->right);
    if(node->right==NULL)
        return findReplace(node->left);
    return findReplace(findNext(node));
}

//删除节点的函数
RBTNode* delete(RBTNode* root,int val)
{
    RBTNode* p=root;
    while(p!=NULL&&p->val!=val)
    {
        if(p->val>val)
            p=p->left;
        else
            p=p->right;
    }
    if(p==NULL) //没有要删除的数值
        return root;
    //使用删除replaceNode替代删除p
    RBTNode* replaceNode=findReplace(p);
    int tmp=replaceNode->val;
    replaceNode->val=p->val;
    p->val=tmp;
    p=replaceNode;
    RBTNode* parent=p->parent;
    if(p->color==RED) //p是红色的节点，删除不破坏平衡
    {
        if(parent!=NULL) //将parent指向p的指针变为null
        {
            if(parent->left==p)
                parent->left=NULL;
            else
                parent->right=NULL;
        }
        free(p);
    }
    RBTNode*out=deleteBalance(p,root);
    if(out->parent!=NULL)
    {
        if(out==parent->left)
            parent->left=NULL;
        else
            parent->right=NULL;
    }
    free(p);
    return out;
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

//检查每一个节点的左右子节点的parent
//指针是不是都指向自己。
bool checkParent(RBTNode* root)
{
    if(root==NULL)
        return true;
    if(root->left!=NULL)
    {
        if(root->left->parent!=root)
        {
            printf("%d -> %d parent error\n",root->val,root->left->val);
            return false;
        }
        if(!checkParent(root->left))
            return false;
    }
    if(root->right!=NULL)
    {
        if(root->right->parent!=root)
        {
            printf("%d -> %d parent error\n",root->val, root->right->val);
            return false;
        }
        if(!checkParent(root->right))
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
    {
        printf("root is not black\n");
        return false;
    }
    if(!checkParent(root))
    {
        printf("parent error\n");
        return false;
    }
    if(!blackBalance(root))
    {
        printf("black path error\n");
        return false;
    }
    if(!checkRBTSub(root))
    {
        printf("red child error\n");
        return false;
    }
    return true;
}

//输出红黑树的结构的函数
void printRBT(RBTNode* root,int depth)
{
    if(root==NULL||depth>3)
        return;
    printf("node: %d color: ",root->val);
    if(root->color==BLACK)
        printf("black ");
    else
        printf("red");
    if(root->parent!=NULL)
        printf(" parent: %d ",root->parent->val);
    else
        printf("parent: null "); 
    if(root->left!=NULL)
        printf("left: %d ",root->left->val);
    else
        printf("left: null ");
    if(root->right!=NULL)
        printf("right: %d\n",root->right->val);
    else
        printf("right: null\n");
    printRBT(root->left,depth+1);
    printRBT(root->right,depth+1);
}

int main()
{
    RBTNode* root=NULL;
    root=insert(root,1);
    root=insert(root,2);
    root=insert(root,3);
    root=insert(root,4);
    root=insert(root,5);
    root=insert(root,14);
    root=insert(root,12);
    root=insert(root,15);
    root=insert(root,8);
    printf("%d\n",checkRBT(root));
    printRBT(root,0);
    root=insert(root,9);
    printf("\n\n");
    printf("%d\n",checkRBT(root));
    printRBT(root,0);
    return 0;
}
