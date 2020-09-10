/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void print_int_star(int *list, int len)
{
    for(int i=0;i<len;i++)
        printf("%d ",list[i]);
    putchar('\n');
}

void print_int_2star(int **matrix,int row,int col)
{
    for(int i=0;i<row;i++)
        print_int_star(matrix[i],col);
}

#define max(a,b) (((a)>(b))?(a):(b))

//Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

bool hasCycle(struct ListNode *head) {
    if(head==NULL)
        return false;
    struct ListNode *p=head->next, *q=head;
    while(p!=NULL&&p!=q)
    {
        p=p->next;
        if(p==NULL)
            return false;
        if(p==q)
            return true;
        p=p->next;
        q=q->next;
    }
    return p==q;
}

int main()
{

    return 0;
}
    
