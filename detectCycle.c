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
//the val is not unique

int hash(struct ListNode* head)
{
    unsigned long long h=((unsigned long long)head/4)%1999999;
    return (int)h;
}

struct ListNode *detectCycle(struct ListNode *head) {
    char* table=(char*)malloc(sizeof(char)*2000000);
    memset(table,0,2000000);
    struct ListNode* p=head;
    while(p!=NULL)
    {
        if(table[hash(p)]!=0)
            return p;
        table[hash(p)]=1;
        p=p->next;
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
    head->next->next=head;
    struct ListNode* tmp=detectCycle(head);
    printf("%x\n",tmp);
#endif
    return 0;
}
    
