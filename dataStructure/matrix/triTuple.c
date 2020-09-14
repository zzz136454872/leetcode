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

typedef struct n{
    int row, col,val;
    struct n *next;
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
    out->val=val;
    out->next=NULL;
    return out;
}

void travelTriTuple(node* head)
{
    if(head==NULL)
        return;
    printf("%d rows %d columns %d varibles\n",head->row, head->col, head->val);
    node* tmp=head->next;
    while(tmp!=NULL)
    {
        printf("%d %d %d\n",tmp->row,tmp->col,tmp->val);
        tmp=tmp->next;
    }
    putchar('\n');
}

void travelMatrix(matrix* mat)
{
    printf("%d rows %d columns\n", mat->row, mat->col);
    print_int_2star(mat->data, mat->row, mat->col);
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

node* matrix2triTuple(matrix* mat)
{
    node* triTuple=getNode(mat->row,mat->col,0);
    node* p=triTuple;
    int count=0;
    for(int i=0;i<mat->row; i++)
    {
        for(int j=0;j<mat->col;j++)
        {
            if(mat->data[i][j]!=0)
            {
                p->next=getNode(i,j,mat->data[i][j]);
                p=p->next;
                count++;
            }
        }
    }
    triTuple->val=count;
    return triTuple;
}

matrix* triTuple2matrix(node* triTuple)
{
    node* p=triTuple;
    matrix* mat=getMatrix(p->row, p->col);
    while(p->next!=NULL)
    {
        p=p->next;
        mat->data[p->row][p->col]=p->val;
    }
    return mat;
}

node* transposeTriTuple(node* t1)
{
    node* t2=getNode(t1->col,t1->row,t1->val);
    node* p1,*p2=t2;
    for(int i=0;i<t1->col;i++)
    {
        p1=t1->next;
        while(p1!=NULL)
        {
            if(p1->col==i)
            {
                p2->next=getNode(p1->col, p1->row, p1->val);
                p2=p2->next;
            }
            p1=p1->next;
        }
    }
    return t2;
}

int main()
{
    matrix* mat=getMatrix(3,4);
    mat->data[1][1]=1;
    mat->data[1][2]=2;
    mat->data[0][3]=3;
    travelMatrix(mat);
    node* triTuple=matrix2triTuple(mat);
    travelTriTuple(triTuple);
    node* t2=transposeTriTuple(triTuple);
    travelTriTuple(t2);
    matrix *mat2=triTuple2matrix(t2);
    travelMatrix(mat2);
    return 0;
}
