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
struct ListNode* insertionSortList(struct ListNode* head){
    struct ListNode* p, *q;
    if(head==NULL||head->next==NULL)
        return head;
    p=head;
    q=head->next;
    p->next=NULL;
    struct ListNode *r,*s;
    while(q!=NULL)
    {
        r=q;
        q=q->next;
        if(r->val<=p->val)
        {
            r->next=p;
            p=r;
            continue;
        }
        s=p;
        while(s->next!=NULL&&s->next->val<r->val)
            s=s->next;
        r->next=s->next;
        s->next=r;
    }
    return p;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    //4->2->1->3
    //-1->5->3->4->0
    struct ListNode* head=getListNode(-1);
    head->next=getListNode(5);
    head->next->next=getListNode(3);
    head->next->next->next=getListNode(4);
    head->next->next->next->next=getListNode(0);
    struct ListNode* out=insertionSortList(head);
    travelList(out);
#endif
    return 0;
}
    
