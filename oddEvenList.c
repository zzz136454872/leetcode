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
struct ListNode* oddEvenList(struct ListNode* head){
    if(head==NULL||head->next==NULL)
        return head;
    struct ListNode* ehead=head;
    struct ListNode* etail=head;
    struct ListNode* ohead=head->next;
    struct ListNode* otail=head->next;
    head=head->next->next;
    while(head!=NULL)
    {
        etail->next=head;
        etail=head;
        head=head->next;
        otail->next=head;
        otail=head;
        if(otail!=NULL)
            head=head->next;
    }
    etail->next=ohead;
    if(otail!=NULL)
        otail->next=NULL;
    return ehead;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    struct ListNode* head;
    head=getListNode(1);
    head->next=getListNode(2);
    head->next->next=getListNode(3);
    head->next->next->next=getListNode(4);
    head->next->next->next->next=getListNode(5);
    struct ListNode* out=oddEvenList(head);
    travelList(out);

#endif
    return 0;
}
    
