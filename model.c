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

void print_double_star(double *list, int len)
{
    for(int i=0;i<len;i++)
        printf("%.2lf ",list[i]);
    putchar('\n');
}

#define max(a,b) (((a)>(b))?(a):(b))

//#define testMod
#ifdef testMod
void test() 
{

}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod

#endif
    return 0;
}
    
