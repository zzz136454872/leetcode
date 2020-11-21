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
struct ListNode* sort1(struct ListNode* head, struct ListNode* nextHead)
{
    if(head==nextHead)
        return head;
    if(head->next==nextHead)
    {
        head->next=NULL;
        return head;
    }
    struct ListNode *p1=head, *p2=head;
    while(p1!=nextHead)
    {
        p1=p1->next;
        p2=p2->next;
        if(p1!=nextHead)
            p1=p1->next;
    }
    p1=sort1(head,p2);
    p2=sort1(p2,nextHead);
    struct ListNode* out=NULL,*tail=NULL;
    while(p1!=NULL&&p2!=NULL)
    {
        if(p1->val<p2->val)
        {
            if(out==NULL)
                out=p1;
            else
	            tail->next=p1;
            tail=p1;
            p1=p1->next;
            tail->next=NULL;
        }
        else
        {
            if(out==NULL)
                out=p2;
            else
                tail->next=p2;
            tail=p2;
            p2=p2->next;
            tail->next=NULL;
        }
    }
    if(p1!=NULL)
        tail->next=p1;
    else
        tail->next=p2;
    return out;
}

struct ListNode* sortList(struct ListNode* head){
    if(head==NULL||head->next==NULL)
        return head;
    head=sort1(head, NULL);
    return head;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct ListNode* head=getListNode(-1);
    head->next=getListNode(5);
    head->next->next=getListNode(3);
    head->next->next->next=getListNode(4);
    head->next->next->next->next=getListNode(0);
    struct ListNode* out=sortList(head);
    travelList(out);
#endif
    return 0;
}
    
