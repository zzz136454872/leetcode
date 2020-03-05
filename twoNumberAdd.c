
#include<stdio.h>
#include<stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* getnode(int val)
{
    struct ListNode* a;
    a = (struct ListNode*)malloc(sizeof(struct ListNode));
    a->val=val;
    a->next=NULL;
    return a;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int carry=0;
    struct ListNode *pout=NULL,*p1,*p2,*newnode ,*p;
    p1=l1;
    p2=l2;
    while(p1 != NULL && p2!=NULL)
    {
        carry+=p1->val+p2->val;
        newnode = getnode(carry%10);
        if(pout!=NULL)
            pout->next = newnode;
        else
            p=newnode;
        pout=newnode;
        carry/=10;
        p1=p1->next;
        p2=p2->next;
    }

    while(p1 != NULL)
    {
        carry+=p1->val;
        newnode = getnode(carry%10);
        if(pout!=NULL)
            pout->next = newnode;
        pout=newnode;
        carry/=10;
        p1=p1 -> next;
    }
    
    while(p2 != NULL)
    {
        carry+=p2->val;
        newnode = getnode(carry%10);
        if(pout!=NULL)
            pout->next = newnode;
        pout=newnode;
        carry/=10;
        p2=p2 -> next;
    }

    if(carry > 0)
        pout->next=getnode(carry);
    return p;
}

int main()
{
    struct ListNode* p1=getnode(1);
    struct ListNode* p2 =getnode(2);
    p1->next=getnode(3);
    p2->next=getnode(9);
    struct ListNode *pout = addTwoNumbers(p1,p2);
    struct ListNode *p=pout;
    while(p!=NULL)
    {
        printf("%d, ",p->val);
        p=p->next;
    }
    return 0;
}
    
