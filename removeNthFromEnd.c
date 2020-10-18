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
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* p=head,*q=head;
    int i;
    for(i=0;i<n+1;i++)
    {
        if(p==NULL)
            break;
        p=p->next;
    }
    if(i==0)
        return NULL;
    if(i==n)
    {
        head=head->next;
        free(q);
        return head;
    }
    if(i==n+1)
    {
        while(p!=NULL)
        {
            p=p->next;
            q=q->next;
        }
        p=q->next->next;
        free(q->next);
        q->next=p;
        return head;
    }
    return NULL;
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
    struct ListNode* out=removeNthFromEnd(head,2);
    travelList(out);
#endif
    return 0;
}
    
