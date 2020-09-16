#include<stdio.h>
#include"../../ctools.h"

void shellPass(int* array, int len, int gap)
{
    int tmp,j;
    for(int i=gap;i<len;i++)
    {
        tmp=array[i];
        j=i;
        while(j>=gap&&array[j-gap]>tmp)
        {
            array[j]=array[j-gap];
            j-=gap;
        }
        array[j]=tmp;
    }
}

void shellSort(int* array, int len, int initGap)
{
    while(initGap>=1)
    {
        shellPass(array,len,initGap);
        initGap=(initGap+1)/3;
    }
}

int main()
{
    int array[]={23,4,32,4,3,2,4,3,2,15,4,315,431,5,43,15,43,5,4,3,5,4213,43};
    int len=sizeof(array)/sizeof(int);
    shellSort(array,len,5);
    print_int_star(array,len);
    return 0;
}
