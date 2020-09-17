#include<stdio.h>
#include"../../ctools.h"
#include<stdlib.h>
#include<string.h>

void merge(int* array, int start, int cut, int end)
{
    int *help=(int*)malloc(sizeof(int)*(end-start+1));
    int i=start,j=cut,k=0;
    while(i<cut&&j<end+1)
    {
        if(array[i]<=array[j])
            help[k++]=array[i++];
        else
            help[k++]=array[j++];
    }
    while(i<cut)
        help[k++]=array[i++];
    while(j<end+1)
        help[k++]=array[j++];
    memcpy(array+start,help,sizeof(int)*(end-start+1)),
    free(help);    
}

void mergeSort(int* array, int start, int end)
{
    if(start>=end)
        return ;
    int mid=(start+end)/2;
    mergeSort(array,start,mid);
    mergeSort(array,mid+1,end);
    merge(array,start, mid+1, end);
}

int main()
{
    int array[]={23,4,32,4,3,2,4,3,2,15,4,315,431,5,43,15,43,5,4,3,5,4213,43};
    int len=sizeof(array)/sizeof(int);
    mergeSort(array,0,len-1);
    print_int_star(array,len);
    return 0;
}
