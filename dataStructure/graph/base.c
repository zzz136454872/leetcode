#include<stdio.h>
#include"../../ctools.h"
#include<stdlib.h>
#include<string.h>

typedef struct n{
    int val;
    struct n* next;
    int weight;
} node;

typedef struct nn{
    int n;
    node** data;
} adjacencyList;

typedef struct nnn{
    int n;
    int** data;
} adjacencyMatrix;

node* getNode(int val,int weight)
{
    node* out=(node*)malloc(sizeof(node));
    out->val=val;
    out->next=NULL;
    out->weight=weight;
    return out;
}

adjacencyList* getAdjacencyList(int n)
{
    adjacencyList* out=(adjacencyList*)malloc(sizeof(adjacencyList));
    out->data=(node**)malloc(n*sizeof(node*));
    out->n=n;
    for(int i=0;i<n;i++)
        out->data[i]=getNode(-1,-1);
    // out->val needs to be filled
    return out;
}

adjacencyMatrix* getAdjacencyMatrix(int n)
{
    adjacencyMatrix* out=(adjacencyMatrix*)malloc(sizeof(adjacencyMatrix));
    out->data=(int**)malloc(n*sizeof(int*));
    out->n=n;
    for(int i=0;i<n;i++)
    {
        out->data[i]=(int*)malloc(n*sizeof(int));
        memset(out->data[i],0,n*sizeof(int));
    }
    return out;
}

adjacencyMatrix* adjacencyList2Matrix(adjacencyList *list)
{
    adjacencyMatrix* mat=getAdjacencyMatrix(list->n);
    node* p;
    for(int i=0;i<list->n;i++)
    {
        p=list->data[i]->next;
        while(p!=NULL)
        {
            mat->data[i][p->val]=p->weight;
            p=p->next;
        }
    }
    return mat;
}

adjacencyList* adjacencyMatrix2List(adjacencyMatrix* mat)
{
    adjacencyList* list=getAdjacencyList(mat->n);
    node* p;
    node* q;
    for(int i=0;i<mat->n;i++)
    {
        for(int j=0;j<mat->n;j++)
        {
            if(mat->data[i][j]!=0)
            {
                p=list->data[i];
                while(p->next!=NULL&&p->val<j)
                    p=p->next;
                q=getNode(j,mat->data[i][j]);
                q->next=p->next;
                p->next=q;
            }
        }
    }
    return list;
}

void travelMatrix(adjacencyMatrix* mat)
{
    printf("n=%d\n",mat->n);
    for(int i=0;i<mat->n;i++)
    {
        printf("%d: ",i);
        for(int j=0;j<mat->n;j++)
        {
            if(mat->data[i][j]!=0)
            {
                printf("%d(%d) ",j,mat->data[i][j]);
            }
        }
        putchar('\n');
    }
}

void travelList(adjacencyList* list)
{
    printf("n=%d",list->n);
    node*p;
    for(int i=0;i<list->n;i++)
    {
        p=list->data[i]->next;
        if(p!=NULL)
            printf("\n%d: ",i);
        while(p!=NULL)
        {
            printf("%d(%d) ",p->val,p->weight);
            p=p->next;
        }
    }
    putchar('\n');
}

void setAdjacencyList(adjacencyList* list, int p1, int p2, int weight)
{
    node* p=list->data[p1];
    node* q;
    while(p->next!=NULL&&p->val<p2)
        p=p->next;
    if(weight==0)
    {
        if(p->next!=NULL&&p->next->val==p2)
        {
            q=p->next;
            p->next=q->next;
            free(q);
        }
    }
    else
    {
        if(p->next!=NULL&&p->next->val==p2)
            p->next->weight=weight;
        else
        {
            q=getNode(p2,weight);
            q->next=p->next;
            p->next=q;
        }
    }
}

adjacencyList* reverseAdjacencyList(adjacencyList* list)
{
    adjacencyList* out=getAdjacencyList(list->n);
    node* p;
    for(int i=0;i<list->n;i++)
    {
        p=list->data[i]->next;
        while(p!=NULL)
        {
            setAdjacencyList(out,p->val,i,p->weight);
            p=p->next;
        }
    }
    return out;
}

int main()
{
    adjacencyMatrix* mat=getAdjacencyMatrix(10);
    mat->data[0][1]=2;
    mat->data[1][2]=3;
    mat->data[2][1]=4;
    travelMatrix(mat);
    adjacencyList* list=adjacencyMatrix2List(mat);
    setAdjacencyList(list,1,1,100);
    travelList(list);
    adjacencyMatrix *mat2=adjacencyList2Matrix(list);
    travelMatrix(mat2);
    adjacencyList* list2=reverseAdjacencyList(list);
    travelList(list2);
    return 0;
}
