#include<stdio.h>
#include"../../ctools.h"
#include<stdlib.h>
#include<string.h>

typedef struct l{
    int from;
    int to;
    int weight;
} line;

typedef struct qn{
    line *l;
    struct qn* next;
} queueNode;

typedef struct {
    queueNode* head, *tail;
    int size;
} lineQueue;

typedef struct n{
    int val;
    struct n* next;
    int weight;
} node;

typedef struct nn{
    int n;
    node** data;
} adjacencyList;

line* getLine(int from, int to, int weight)
{
    line* out=(line*)malloc(sizeof(line));
    out->from=from;
    out->to=to;
    out->weight=weight;
    return out;
}

lineQueue* getLineQueue()
{
    lineQueue* out=(lineQueue*)malloc(sizeof(lineQueue));
    out->size=0;
    out->head=NULL;
    out->tail=NULL;
    return out;
}

queueNode* getQueueNode(line* l)
{
    queueNode* out=(queueNode*)malloc(sizeof(queueNode));
    out->next=NULL;
    out->l=l;
    return out;
}

void enqueue(lineQueue* lq,line* l)
{
    if(lq==NULL)
        return;
    if(lq->size==0)
    {
        lq->tail=getQueueNode(l);
        lq->head=lq->tail;
    }
    else
    {
        lq->tail->next=getQueueNode(l);
        lq->tail=lq->tail->next;
    }
    lq->size++;
}

line* dequeue(lineQueue* lq)
{
    if(lq==NULL||lq->size==0)
        return NULL;
    queueNode* p=lq->head;
    line* out=p->l;
    lq->head=p->next;
    free(p);
    lq->size--;
    return out;
}

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

lineQueue* prim(adjacencyList* list)
{
    int *visited=(int*)malloc(sizeof(int)*list->n);
    memset(visited, 0,sizeof(int)*list->n);
    visited[0]=1;
    lineQueue* lq=getLineQueue();
    int *distance=(int*)malloc(sizeof(int)*list->n);
    int *pre=(int*)malloc(sizeof(int)*list->n);
    for(int i=0;i<list->n;i++)
    {
        distance[i]=123456;
        pre[i]=-1;
    }
    node* p=list->data[0]->next;
    while(p!=NULL)
    {
        distance[p->val]=min(distance[p->val],p->weight);
        pre[p->val]=0;
        p=p->next;
    }
    print_int_star(distance,list->n);
    print_int_star(pre,list->n);
    print_int_star(visited,list->n);
    int minDistance=123456;
    int minLoc=0;
    for(int i=0;i<list->n-1;i++)
    {
        minDistance=123456;
        minLoc=-1;
        for(int j=0;j<list->n;j++)
        {
            if(visited[j])
                continue;
            if(minDistance>distance[j])
            {
                minDistance=distance[j];
                minLoc=j;
            }
        }
        if(minLoc==-1)
            break;
        visited[minLoc]=1;
        enqueue(lq,getLine(pre[minLoc],minLoc,minDistance));
        p=list->data[minLoc]->next;
        while(p!=NULL)
        {
            if(distance[p->val]>p->weight)
            {
                distance[p->val]=p->weight;
                pre[p->val]=minLoc;
            }
            p=p->next;
        }
    }
    free(visited);
    free(pre);
    free(distance);
    return lq;
}

void travelLineQueue(lineQueue* lq)
{
    queueNode* qn=lq->head;
    printf("%d lines\n",lq->size);
    while(qn!=NULL)
    {
        printf("%d -> %d : %d\n",qn->l->from, qn->l->to,qn->l->weight);
        qn=qn->next;
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
    lineQueue* lq=prim(list);
    travelLineQueue(lq);
    return 0;
}
