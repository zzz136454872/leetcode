#ifndef clist_h
#define clist_h
#include<stdio.h>
#include<stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* getListNode(int val)
{
    struct ListNode* out=(struct ListNode*)malloc(sizeof(struct ListNode));
    out->val=val;
    out->next=NULL;
    return out;
}

void travelList(struct ListNode* head)
{
    if(head==NULL)
    {
        putchar('\n');
        return;
    }
    printf("%d ",head->val);
    travelList(head->next);
}

#endif
