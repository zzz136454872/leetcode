#ifndef ctool_h
#define ctool_h
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define bool int
#define true 1
#define false 0

void print_int_star(int *list, int len)
{
	int i;
    for(i=0;i<len;i++)
        printf("%d ",list[i]);
    putchar('\n');
}

void print_int_2star(int **matrix,int row,int col)
{
	int i;
    for(i=0;i<row;i++)
        print_int_star(matrix[i],col);
}

void print_double_star(double *list, int len)
{
	int i;
    for(i=0;i<len;i++)
        printf("%.2lf ",list[i]);
    putchar('\n');
}

void print_char_2star(char** strings, int len)
{
	int i;
    for(i=0;i<len;i++)
    {
        printf("%s ",strings[i]);
    }
    putchar('\n');
}

void printmem(void* mem,int length)
{
    unsigned char* pmem=(unsigned char*)mem;
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

char** malloc_char_2star(char* a,int size1,int size2) {
    char** res=(char**)malloc(sizeof(char*)*size1);
    for(int i=0;i<size1;i++) {
        res[i]=(char*)malloc(sizeof(char)*(strlen(a+i*size2)+1));
        strcpy(res[i],a+i*size2);
    }
    return res;
}

#endif
