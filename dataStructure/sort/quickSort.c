#include<stdio.h>
#include"../../ctools.h"

void quickSort(int* array, int start, int end)
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
    quickSort(array,start,i-1);
    quickSort(array,i+1,end);
}

int main()
{
    int array[]={1,1,1,1,1,1,1,1,1,1,1,1,1,1};
    int len=sizeof(array)/sizeof(int);
    quickSort(array,0,len-1);
    print_int_star(array,len);
    return 0;
}
