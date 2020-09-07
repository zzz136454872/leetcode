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

int hIndex(int* citations, int citationsSize){
    int *log=(int*)malloc((citationsSize+1)*sizeof(int));
    for(int i=0;i<citationsSize+1;i++)
        log[i]=0;
    for(int i=0;i<citationsSize;i++)
    {
        if(citations[i]<citationsSize)
            log[citations[i]]++;
        else
            log[citationsSize]+=1;
    }
    for(int i=citationsSize-1;i>=0;i--)
        log[i]+=log[i+1];
    for(int i=0;i<citationsSize+1;i++)
    {
        if(log[i]<i)
            return i-1;
    }
    return citationsSize;
}

int main()
{
    int len=1;
    int citations[1] = {0};
    int out=hIndex(citations,len);
    printf("%d\n",out);
    return 0;
}
    
