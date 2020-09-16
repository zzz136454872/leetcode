#include<stdio.h>
#include"../../ctools.h"
#include<stdlib.h>
#include<string.h>
#define INF 123456

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
    adjacencyList* list;
    int* pre;
    int start;
} minPath;

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
    // out->val and out->weight needs to be filled
    return out;
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

minPath* dijkstra(adjacencyList* list,int p0)
{
    int *pre=(int*)malloc(list->n*sizeof(int));
    int *distance=(int*)malloc(list->n*sizeof(int));
    int *visited=(int*)malloc(list->n*sizeof(int));
    for(int i=0;i<list->n;i++)
    {
        pre[i]=-1;
        distance[i]=INF;
        visited[i]=0;
    }
    visited[p0]=1;
    distance[p0]=0;
    node* p=list->data[p0]->next;
    while(p!=NULL)
    {
        if(p->weight<distance[p->val])
        {
            distance[p->val]=p->weight;
            pre[p->val]=p0;
        }
        p=p->next;
    }
    int minDistance;
    int minLoc;
    for(int i=0;i<list->n-1;i++)
    {
        if(visited[i])
            continue;
        minDistance=INF;
        minLoc=-1;
        for(int j=0;j<list->n;j++)
        {
            if(distance[i]<minDistance)
            {
                minDistance=distance[i];
                minLoc=i;
            }
        }
        if(minLoc==-1)
            break;
        visited[minLoc]=1;
        p=list->data[minLoc]->next;
        while(p!=NULL)
        {
            if(distance[p->val]>p->weight+distance[minLoc])
            {
                distance[p->val]=p->weight+distance[minLoc];
                pre[p->val]=minLoc;
            }
            p=p->next;
        }
    }
    free(distance);
    free(visited);
    minPath *mp=(minPath*)malloc(sizeof(minPath));
    mp->list=list;
    mp->pre=pre;
    mp->start=p0;
    return mp;
}

void showMinPath(minPath* mp)
{
    int end;
    for(int i=0;i<mp->list->n;i++)
    {
        end=i;
        while(end!=-1)
        {
            printf("%d",end);
            end=mp->pre[end];
            if(end!=-1)
                printf(" -> ");
        }
        putchar('\n');
    }
}

int main()
{
    adjacencyList* list=getAdjacencyList(4);
    setAdjacencyList(list,0,1,2);
    setAdjacencyList(list,1,0,2);
    setAdjacencyList(list,0,2,3);
    setAdjacencyList(list,2,0,3);
    setAdjacencyList(list,1,2,4);
    setAdjacencyList(list,2,1,4);
    setAdjacencyList(list,2,3,100);
    travelList(list);
    minPath* mp=dijkstra(list,1);
    showMinPath(mp);
    return 0;
}
