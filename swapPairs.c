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
struct ListNode* swapPairs(struct ListNode* head)
{
    struct ListNode* p=head,*nxt=NULL, *pre=NULL;
    if(head==NULL||head->next==NULL)
        return head;
    else
        head=head->next;
    while(p!=NULL&&p->next!=NULL)
    {
        nxt=p->next->next;
        if(pre!=NULL)
            pre->next=p->next;
        p->next->next=p;
        p->next=nxt;
        pre=p;
        p=nxt;
    }
    return head;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    //struct ListNode* head=getListNode(1);
    struct ListNode* head=NULL;
    //head->next=getListNode(2);
    //head->next->next=getListNode(3);
    //head->next->next->next=getListNode(4);
    struct ListNode* out=swapPairs(head);
    travelList(out);
#endif
    return 0;
}
    
