/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include"ctools.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"clist.h"

//#define testMod
#ifdef testMod
void test() 
{

}
#endif

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

#ifndef testMod
struct ListNode* revList(struct ListNode* list)
{
    if(list==NULL||list->next==NULL)
        return list;
    struct ListNode* p=list, *q=list->next, *r=q->next;
    p->next=NULL;
    q->next=p;
    while(r!=NULL)
    {
    	p=q;
        q=r;
        r=r->next;
        q->next=p;
    }
    return q;
}

void reorderList(struct ListNode* head){
    if(head==NULL)
        return;
    struct ListNode* p=head,*q=head;
    while(p!=NULL)
    {
        p=p->next;
        if(p!=NULL)
        {
            p=p->next;
            q=q->next;
        }
    }
    p=q->next;
    q->next=NULL;
    p=revList(p);
    q=head;
    struct ListNode* r=head;
    q=q->next;
    while(p!=NULL&&q!=NULL)
    {
        r->next=p;
        r=r->next;
        p=p->next;
        r->next=q;
        q=q->next;
        r=r->next;
    }
    if(p!=NULL)
    {
        r->next=p;
        r=r->next;
    }
    if(q!=NULL)
    {
        r->next=q;
        r=r->next;
    }
    r->next=NULL;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct ListNode* head=getListNode(1);
    head->next=getListNode(2);
    head->next->next=getListNode(3);
    head->next->next->next=getListNode(4);
    head->next->next->next->next=getListNode(5);
    head->next->next->next->next->next=getListNode(6);
    head->next->next->next->next->next->next=getListNode(7);
    reorderList(head);
    travelList(head);
#endif
    return 0;
}
    
