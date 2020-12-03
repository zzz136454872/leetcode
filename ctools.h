#ifndef ctool_h
#define ctool_h
#include<stdio.h>

#define bool int
#define true 1
#define false 0

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

void print_char_2star(char** strings, int len)
{
    for(int i=0;i<len;i++)
    {
        printf("%s ",strings[i]);
    }
    putchar('\n');
}

void printmem(void* mem,int length)
{
    unsigned char* pmem=mem;
    int i;
    for(i=0;i<length;i++)
    {
        printf("%x ",pmem[i]);
        if(i%16==15)
            putchar('\n');
    }
    if(i%16!=0)
        putchar('\n');
}

#endif
