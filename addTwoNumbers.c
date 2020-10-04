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
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int carry=0;
    int now;
    struct ListNode* out=NULL;
    struct ListNode* tail=NULL;
    while(l1!=NULL||l2!=NULL||carry!=0)
    {
        now=carry;
        if(l1!=NULL)
        {
            now+=l1->val;
            l1=l1->next;
        }
        if(l2!=NULL)
        {
            now+=l2->val;
            l2=l2->next;
        }
        carry=now/10;
        now=now%10;
        if(tail==NULL)
        {
            out=getListNode(now);
            tail=out;
        }
        else
        {
            tail->next=getListNode(now);
            tail=tail->next;
        }
    }
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct ListNode* head1=getListNode(2);
    head1->next=getListNode(4);
    head1->next->next=getListNode(3);
    struct ListNode* head2=getListNode(5);
    head2->next=getListNode(6);
    head2->next->next=getListNode(7);
    struct ListNode* out=addTwoNumbers(head1,head2);
    travelList(out);
#endif
    return 0;
}
    
