#include<stdio.h>
#include"../../ctools.h"
#include<stdlib.h>

void adjust(int* array, int len, int i)
{
    int j=2*i+1;
    int tmp;
    if(j>=len)
        return;
    if(j<len-1&&array[j+1]>array[j])
        j++;
    if(array[j]>array[i])
    {
        tmp=array[i];
        array[i]=array[j];
        array[j]=tmp;
        adjust(array,len,j);
    }
}

int heapPop(int* array, int len)
{
    int tmp=array[0];
    array[0]=array[len-1];
    adjust(array,len,0);
    return tmp;
}

void heapSort(int* array, int len)
{
    for(int i=(len-2)/2;i>=0;i--)
        adjust(array,len,i);
    for(int i=0;i<len-1;i++)
        array[len-i-1]=heapPop(array,len-i);
}

int main()
{
    int array[]={143,41,3,41324,12,34,321,4,321,4,3214,3,124,3,21,4,321,4,321,4,132};
    int len=sizeof(array)/sizeof(int);
    heapSort(array,len);
    print_int_star(array,len);
    return 0;
}

