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

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int combineNum(int n, int k)
{
    int out=1;
    for(int i=0;i<k;i++)
        out=out*(n-i)/(i+1);
    return out;
}

int **combineSub(int n, int k, int min, int kSub, int* retSize)
{
    int i,j;

    if(n-min+1<kSub)
    {
        *retSize=0;
        return NULL;
    }

    int outSize=combineNum(n-min+1, kSub);
    *retSize=outSize;
    int **out=(int**)malloc(sizeof(int*)*outSize);

    if(kSub==1)
    {
        for(i=0;i<outSize;i++)
        {
            out[i]=(int*)malloc(sizeof(int)*k);
            out[i][0]=min+i;
        }
        return out;
    }

    j=0;
    for(i=min;i<n;i++)
    {
        int rsize;
        int **tmp=combineSub(n,k,i+1, kSub-1, &rsize);
        if(rsize==0)
            break;
        for(int m=0;m<rsize;m++)
        {
            tmp[m][kSub-1]=i;
            out[j++]=tmp[m];
        }
        free(tmp);
    }
    return out;
}

int** combine(int n, int k, int* returnSize, int** returnColumnSizes){
    int **out=combineSub(n,k,1,k,returnSize);
    int *columnSizes=(int*)malloc(sizeof(int)*(*returnSize));
    *returnColumnSizes=columnSizes;
    for(int i=0;i<*returnSize;i++)
        columnSizes[i]=k;
    return out;
}

int main()
{
    int returnSize;
    int n=4;
    int k=2;
    int *returnColumnSizes;
    int **out=combine(n,k,&returnSize,&returnColumnSizes);
    print_int_2star(out,returnSize,returnColumnSizes[0]);
    return 0;
}
    
