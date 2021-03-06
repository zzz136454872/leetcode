#include<stdio.h>
#include"../../ctools.h"
#include<stdlib.h>
#include<string.h>

#define BUFFERSIZE 100

typedef struct n{
    int val;
    struct n* next;
    int weight;
} node;

typedef struct nn{
    int n;
    node** data;
} adjacencyList;

typedef struct {
    int buffer[BUFFERSIZE];
    int size;
} array;

array* getArray()
{
    array* out=(array*)malloc(sizeof(array));
    out->size=0;
    for(int i=0;i<BUFFERSIZE;i++)
        out->buffer[i]=0;
    return out;
}

void push(array* s,int val)
{
    if(s==NULL)
        return;
    s->buffer[s->size++]=val;
}

int pop(array* s)
{
    if(s==NULL||s->size==0)
        return -1;
    return s->buffer[--(s->size)];
}

void travelArray(array* a)
{
    if(a==NULL)
        return;
    printf("total: %d nums\n", a->size);
    for(int i=0;i<a->size;i++)
        printf("%d ", a->buffer[i]);
    putchar('\n');
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

int* getInDegree(adjacencyList* list)
{
    int* inDegree=(int*)malloc(sizeof(int)*list->n);
    memset(inDegree,0,sizeof(int)*list->n);
    node* p;
    for(int i=0;i<list->n;i++)
    {
        p=list->data[i]->next;
        while(p!=NULL)
        {
            inDegree[p->val]++;
            p=p->next;
        }
    }
    return inDegree;
}

array* topologicalSort(adjacencyList* list)
{
    int* inDegree=getInDegree(list);
    array* stack=getArray();
    array* tmpStack=getArray();
    int now;
    node* p;
    for(int i=0;i<list->n;i++)
    {
        if(inDegree[i]==0)
        {
            push(stack,i);
            push(tmpStack,i);
        }
    }
    while(tmpStack->size>0)
    {
        now=pop(tmpStack);
        p=list->data[now]->next;
        while(p!=NULL)
        {
            inDegree[p->val]--;
            if(!inDegree[p->val])
            {
                push(stack,p->val);
                push(tmpStack,p->val);
            }
            p=p->next;
        }
    }
    free(inDegree);
    return stack;
}

void freeLinkedList(node* n)
{
    if(n==NULL)
        return;
    freeLinkedList(n->next);
    free(n);
}

void freeAdjacencyList(adjacencyList* list)
{
    for(int i=0;i<list->n;i++)
        freeLinkedList(list->data[i]);
    free(list);
}

array* criticalPath(adjacencyList* list)
{
    array* forward=topologicalSort(list);
    if(forward->size!=list->n)
    {
        free(forward);
        return NULL;
    }
    int* firstTime=(int*)malloc(sizeof(int)*list->n);
    memset(firstTime, 0, sizeof(int)*list->n);
    adjacencyList* reverseList=reverseAdjacencyList(list);
    array* backward=topologicalSort(reverseList);
    int time=0;
    node* p;
    int now;
    for(int i=0;i<list->n;i++)
    {
        now=forward->buffer[i];
        time=0;
        p=reverseList->data[now]->next;
        while(p!=NULL)
        {
            time=max(time,firstTime[p->val]+p->weight);
            p=p->next;
        }
        firstTime[now]=time;
    }
    int totalTime=firstTime[forward->buffer[forward->size-1]];
    int *latestTime=(int*)malloc(sizeof(int)*list->n);
    for(int i=0;i<list->n;i++)
        latestTime[i]=totalTime;
    for(int i=0;i<list->n;i++)
    {
        now=backward->buffer[i];
        time=totalTime;
        p=list->data[now]->next;
        while(p!=NULL)
        {
            time=min(time, latestTime[p->val]-p->weight);
            p=p->next;
        }
        latestTime[now]=time;
    }
    array* out=getArray();
    for(int i=0;i<list->n;i++)
    {
        now=forward->buffer[i];
        if(firstTime[now]==latestTime[now])
        {
            push(out,now);
        }
    }
    free(firstTime);
    free(latestTime);
    free(forward);
    free(backward);
    freeAdjacencyList(reverseList);
    return out;
}

int main()
{
    adjacencyList* list=getAdjacencyList(4);
    setAdjacencyList(list,0,1,200);
    setAdjacencyList(list,3,1,2);
    setAdjacencyList(list,0,2,3);
    setAdjacencyList(list,2,1,4);
    setAdjacencyList(list,2,3,100);
    travelList(list);
    //array* a=topologicalSort(list);
    array* a=criticalPath(list);
    travelArray(a);
    return 0;
}


