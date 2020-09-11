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

int count(int n)
{
    int out=0;
    while(n>0)
    {
        out+=n&1;
        n>>=1;
    }
    return out;
}

int add(int n)
{
    int out=0;
    for(int i=1;i<10&&n>0;i++)
    {
        out+=(i)*(n&1);
        n>>=1;
    }
    return out;
}

int* find(int num, int k)
{
    int* out=(int*)malloc(sizeof(int)*k);
    int j=0;
    for(int i=1;i<10&&num>0;i++)
    {
        if(num&1)
            out[j++]=i;
        num>>=1;
    }
    return out;
}

//Return an array of arrays of size *returnSize.
//The sizes of the arrays are returned as *returnColumnSizes array.
//Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().

int** combinationSum3(int k, int n, int* returnSize, int** returnColumnSizes){
    int outSize=0;
    int bufferSize=2;
    int **out=(int**)malloc(sizeof(int*)*511);
    for(int i=1;i<512;i++)
    {
        if(count(i)==k)
        {
            if(add(i)==n)
            {
                out[outSize++]=find(i,k);
            }
        }
    }
    *returnSize=outSize;
    *returnColumnSizes=(int*)malloc(outSize*sizeof(int));
    for(int i=0;i<outSize;i++)
        (*returnColumnSizes)[i]=k;
    return out;
}

int main()
{
    int outSize;
    int *returnColumnSizes;
    int i=4;
    int** out=combinationSum3(3,9,&outSize, &returnColumnSizes);
    print_int_2star(out,outSize, 3);
    return 0;
}

