#include<stdio.h>
#include"../../ctools.h"
#include<stdlib.h>
#include<string.h>

typedef struct n {
    int row,col;
    struct n* right, *down;
    union {
        struct n *next;
        int val;
    };
} node;

typedef struct m{
    int row, col;
    int **data;
} matrix;

node* getNode(int row, int col, int val)
{
    node* out=(node*)malloc(sizeof(node));
    out->row=row;
    out->col=col;
    out->right=NULL;
    out->down=NULL;
    out->val=val;
    return out;
}

matrix* getMatrix(int row, int col)
{
    matrix *out=(matrix*)malloc(sizeof(matrix));
    out->row=row;
    out->col=col;
    out->data=(int**)malloc(sizeof(int*)*row);
    for(int i=0;i<row;i++)
    {
        out->data[i]=(int*)malloc(sizeof(int)*col);
        memset(out->data[i],0,sizeof(int)*col);
    }
    return out;
}

void travelMatrix(matrix* mat)
{
    printf("%d rows %d columns\n", mat->row, mat->col);
    print_int_2star(mat->data, mat->row, mat->col);
}


node* matrix2LinkedMatrix(matrix* mat)
{
    int s=max(mat->row, mat->col)+1;
    node* head=(node*)malloc(s*sizeof(node));
    head->row=mat->row;
    head->col=mat->col;
    int i;
    for(i=1;i<s;i++)
    {
        head[i-1].next=head+i;
        head[i].row=0;
        head[i].col=0;
        head[i].right=head+i;
        head[i].down=head+i;
    }

    head[s-1].next=head;
    node* p;
    node* newNode;
    for(i=0;i<mat->row;i++)
    {
        for(int j=0;j<mat->col;j++)
        {
            if(mat->data[i][j]!=0)
            {
                newNode=getNode(i,j,mat->data[i][j]);
                p=head+i+1;
                while(p->right!=head+i+1&&p->col<j)
                    p=p->right;
                newNode->right=p->right;
                p->right=newNode;
                p=head+j+1;
                while(p->down!=head+j+1&&p->row<i)
                    p=p->down;
                newNode->down=p->down;
                p->down=newNode;
            }
        }
    }
    return head;
}

void travelLinkedMatrix(node* head)
{
    printf("%d row %d column\n", head->row, head->col);
    if(head==NULL)
        return;
    node* p;
    for(int i=0;i<head->row;i++)
    {
        p=head+i+1;
        while(p->right!=head+i+1)
        {
            p=p->right;
            printf("%d %d %d\n",p->row,p->col,p->val);
        }
    }
}

int main()
{
    matrix* mat=getMatrix(3,4);
    mat->data[1][1]=1;
    mat->data[1][2]=2;
    mat->data[0][3]=3;
    travelMatrix(mat);
    node* linkedMat=matrix2LinkedMatrix(mat);
    travelLinkedMatrix(linkedMat);
    return 0;
}
