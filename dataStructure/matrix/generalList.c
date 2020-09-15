#include<stdio.h>
#include"../../ctools.h"
#include<ctype.h>
#include<stdlib.h>
#include<string.h>

#define list 0
#define element 1

typedef struct n{
    int tag;
    struct n* next;
    union {
        struct n* sub;
        int val;
    };
} node;

node* getNode()
{
    node* out=(node*)malloc(sizeof(node));
    out->tag=list;
    out->next=NULL;
    out->sub=NULL;
    return out;
}

node* getGeneralList(char* str)
{
    //printf("enter: %s\n", str);
    if(str[0]!='(')
        return NULL;
    node*head=getNode();
    char buffer[100];
    int i=1;
    node*p=head;
    while(i<strlen(str)-1)
    {
        if(str[i]=='(')
        {
            int j=i+1;
            int log=1;
            while(log!=0)
            {
                if(str[j]==')')
                    log--;
                else if(str[j]=='(')
                    log++;
                j++;
            }
            strncpy(buffer,str+i,j-i);
            p->next=getNode();
            p=p->next;
            //printf("call sub\n");
            p->sub=getGeneralList(buffer);
            //printf("return from sub\n");
            i=j+1;
        }
        else if(isdigit(str[i]))
        {
            int tmp=0;
            while(isdigit(str[i]))
                tmp=tmp*10+(str[i++]-'0');
            p->next=getNode();
            p->next->tag=element;
            p->next->val=tmp;
            p=p->next;
        }
        else
            i++;
    }
    return head;
}

void travelGeneralList(node* generalList)
{
    if(generalList==NULL)
        return;
    putchar('(');
    node* p=generalList->next;
    while(p!=NULL)
    {
        if(p->tag==list)
            travelGeneralList(p->sub);
        else
            printf("%d",p->val);
        p=p->next;
        if(p!=NULL)
            putchar(',');
    }
    putchar(')');
}

int main()
{
    char exp[]="(1,(2,(3)))";
    node* head=getGeneralList(exp);
    travelGeneralList(head);
    return 0;
}
