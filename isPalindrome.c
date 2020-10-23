#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include"clist.h"
#include"ctools.h"

bool isPalindrome1(int x){
    if(x < 0)
        return false;
    if(x == 0)
        return true;
    char tmp[20]={0};
    int i=0;
    while(i>0)
    {
        tmp[i++]=x % 10 + '0';
        x/=10;
    }
    i--;
    int j=0;
    while(tmp[i]==tmp[j])
    {
        i--;
        j++;
        if(i >= j)
            return true;
    }
    return false;
}

//回文链表
bool isPalindrome(struct ListNode* head){
    int bufferSize=2;
    int *buffer=(int*)malloc(sizeof(int)*bufferSize);
    struct ListNode* p;
    p=head;
    int i=0;
    while(p!=NULL)
    {
        if(i==bufferSize)
        {
            bufferSize*=2;
            buffer=(int*)realloc(buffer,sizeof(int)*bufferSize);
        }
        buffer[i++]=p->val;
        p=p->next;
    }
    int j=i-1;
    i=0;
    bool out=true;
    while(i<j)
    {
        if(buffer[i]!=buffer[j])
        {
            out=false;
            break;
        }
        i++;
        j--;
    }
    return out;
}

int main()
{
    //char a[]="1234321";
    //int b=isPalindrome(a);
    struct ListNode* head=getListNode(1);
    head->next=getListNode(2);
    head->next->next=getListNode(2);
    head->next->next->next=getListNode(1);
    printf("%d\n",isPalindrome(head));
    return 0;
}
