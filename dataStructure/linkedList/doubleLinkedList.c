#include<stdio.h>
#include<stdlib.h>

typedef struct n {
    int val;
    struct n *l,*r;
} node;

node* getNode(int val)
{
    node* out=(node*)malloc(sizeof(node));
    out->val=val;
    out->l=NULL;
    out->r=NULL;
    return out;
}

node* createDoubleLinkedList(int *list, int len)
{
    node *head=NULL, *p=NULL;
    for(int i=0;i<len;i++)
    {
        if(head==NULL)
        {
            head=getNode(list[i]);
            p=head;
        }
        else
        {
            p->r=getNode(list[i]);
            p->r->l=p;
            p=p->r;
        }
    }
    return head;
}

void travelLeft(node* head)
{
    while(head!=NULL)
    {
        printf("%d ",head->val);
        head=head->r;
    }
    putchar('\n');
}

void travelRight(node* tail)
{
    while(tail!=NULL)
    {
        printf("%d ",tail->val);
        tail=tail->l;
    }
    putchar('\n');
}

node* delete(node* head, int loc)
{
    node* l=head, *now, *r;
    if(head==NULL)
        return NULL;
    if(loc==0)
    {
        r=head->r;
        free(head);
        if(r!=NULL)
            r->l=NULL;
        return r;
    }
    while(loc-->1&&l!=NULL)
        l=l->r;
    if(l==NULL)
        return head;
    now=l->r;
    if(now==NULL)
        return head;
    r=now->r;
    free(now);
    l->r=r;
    if(r!=NULL)
        r->l=l;
    return head;
}

node* insert(node* head,  int loc, int val)
{
    node* tmp=getNode(val);
    if(loc==0)
    {
        if(head!=NULL)
        {
            tmp->r=head;
            head->l=tmp;
        }
        return tmp;
    }
    node* p=head, *q;
    while(loc-->1&&p!=NULL)
        p=p->r;
    if(p==NULL)
        return head;
    q=p->r;
    p->r=tmp;
    tmp->l=p;
    tmp->r=q;
    if(q!=NULL)
        q->l=tmp;
    return head;
}

int main()
{
    int nums[4]={1,2,3,4};
    node* list=createDoubleLinkedList(nums,4);
    node* tmp=list;
    tmp=tmp->r;
    tmp=tmp->r;
    tmp=tmp->r;
    travelLeft(list);
    list=insert(list, 4, 5);
    travelLeft(list);
    list=delete(list, 4);
    travelLeft(list);
    return 0;
}
