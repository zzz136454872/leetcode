#include<stdio.h>
#include"../../ctools.h"

void quickSortMain(int* array, int start, int end)
{
    if(start>=end)
        return;
    int i=start,j=end;
    int flag=array[start];
    while(i<j)
    {
        while(i<j&&array[j]>=flag)
            j--;
        array[i]=array[j];
        while(i<j&&array[i]<=flag)
            i++;
        array[j]=array[i];
    }
    array[i]=flag;
    quickSortMain(array,start,i-1);
    quickSortMain(array,i+1,end);
}

void quickSort(int* arr,int len)
{
    quickSortMain(arr,0,len-1);
}

int main()
{
    int array[]={1,1,3,1,1,1,1,1,1,1,1,1,1,1};
    int len=sizeof(array)/sizeof(int);
    quickSort(array,len);
    print_int_star(array,len);
    return 0;
}
