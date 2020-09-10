#include<stdio.h>
#include<stdlib.h>

typedef struct n{
    int val;
    struct n* next;
} node;

node* getNode(int val)
{
    node* out=(node*)malloc(sizeof(node));
    out->val=val;
    out->next=NULL;
    return out;
}

node* createCycularList(int* pint, int len)
{
    node* head=NULL, *now;
    for(int i=0;i<len;i++)
    {
        if(i==0)
        {
            head=getNode(pint[0]);
            now=head;
        }
        else
        {
            now->next=getNode(pint[i]);
            now=now->next;
        }
        now->next=head;
    }
    return head;
}

void travel(node* head)
{
    if(head==NULL)
        return;
    printf("%d ",head->val);
    node* tmp=head->next;
    while(tmp!=head)
    {
        printf("%d ",tmp->val);
        tmp=tmp->next;
    }
    putchar('\n');
}

node* find(node* head,int val)
{
    if(head==NULL||head->val==val)
        return head;
    node* tmp=head->next;
    while(tmp!=head)
    {
        if(tmp->val==val)
            return tmp;
    }
    return NULL;
}

node *insert(node* head,int loc,int val)
{
    node* p=NULL;
    if(head==NULL)
    {
        p=getNode(val);
        p->next=p;
        return p;
    }
    if(loc==0)
    {
        p=head;
        while(p->next!=head)
            p=p->next;
        p->next=getNode(val);
        p=p->next;
        p->next=head;
        return p;
    }
    p=head;
    for(int i=0;i<loc-1;i++)
        p=p->next;
    node* q;
    q=p->next;
    p->next=getNode(val);
    p->next->next=q;
    return head;
}

node* delete(node* head, int loc)
{
    if(head==NULL)
        return NULL;
    if(head->next==head)
    {
        free(head);
        return NULL;
    }
    node* p=head,*q;
    if(loc==0)
    {
        while(p->next!=head)
        {
            p=p->next;
        }
        head=head->next;
        free(p->next);
        p->next=head;
        return head;
    }
    while(loc-->1)
    {
        p=p->next;
    }
    q=p->next->next;
    free(p->next);
    p->next=q;
    return head;
}

int main()
{
    int test[4]={1,2,3,4};
    node* list=createCycularList(test,4);
    travel(list);
    list=insert(list,2,100);
    travel(list);
    list=delete(list,2);
    travel(list);
    list=delete(list,0);
    travel(list);
    return 0;
}

