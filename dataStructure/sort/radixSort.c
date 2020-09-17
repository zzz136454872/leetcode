#include<stdio.h>
#include"../../ctools.h"
#include<string.h>
#include<stdlib.h>

typedef struct n{
    int val;
    struct n* next;
} node;

node* getNode(int val)
{
    node* out=(node*)malloc(sizeof(node));
    out->val=val;
    out->next=NULL;
    return out;
}

int getNum(int n,int loc)
{
    int base=1;
    for(int i=0;i<loc;i++)
        base*=10;
    return (n/base)%10;
}

int getLen(int n)
{
    int out=0;
    while(n!=0)
    {
        n/=10;
        out++;
    }
    return out;
}

void freeLinkedList(node* a)
{
    if(a==NULL)
        return;
    freeLinkedList(a->next);
    free(a);
}

void radixSort(int* array, int n)
{
    if(n==0)
        return;
    node* p=NULL,*tmp=NULL;
    int maxLen=0;
    for(int i=0;i<n;i++)
    {
        maxLen=max(maxLen, getLen(array[i]));
        if(p==NULL)
		{
            p=getNode(array[i]);
            tmp=p;
        }
        else
        {
            tmp->next=getNode(array[i]);
            tmp=tmp->next;
        }
    }
    node** head=(node**)malloc(sizeof(node*)*10);
    node** tail=(node**)malloc(sizeof(node*)*10);
    memset(head,0,sizeof(node*)*10);
    memset(tail,0,sizeof(node*)*10);
    int num,j;
    for(int i=0;i<maxLen; i++)
    {
        memset(head,0,sizeof(node*)*10);
        memset(tail,0,sizeof(node*)*10);
        while(p!=NULL)
        {
            tmp=p;
            p=p->next;
            tmp->next=NULL;
            num=getNum(tmp->val,i);
            if(head[num]==NULL)
            {
                head[num]=tmp;
                tail[num]=tmp;
            }
            else
            {
                tail[num]->next=tmp;
                tail[num]=tail[num]->next;
            }
        }
        j=0;
        while(head[j]==NULL)
            j++;
        p=head[j];
        tmp=tail[j++];
        while(j<10)
        {
            if(head[j]!=NULL)
            {
                tmp->next=head[j];
                tmp=tail[j];
            }
            j++;
        }
        tmp->next=NULL;
    }
    tmp=p;
    int i=0;
    while(tmp!=NULL)
    {
        array[i++]=tmp->val;
        tmp=tmp->next;
    }
    free(head);
    free(tail);
    freeLinkedList(p);
}

int main()
{
    int array[]={23,4,32,4,3,2,4,3,2,15,4,315,431,5,43,15,43,5,4,3,5,4213,43};
    int len=sizeof(array)/sizeof(int);
    printf("%d\n",len);
    radixSort(array,len);
    print_int_star(array,len);
    return 0;
}
