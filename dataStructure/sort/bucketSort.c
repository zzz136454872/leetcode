#include<stdio.h>
#include"../../ctools.h"
#include<stdlib.h>
#include<string.h>

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

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

void bucketSort(int* arr,int len, void (*subSort)(int*,int))
{
    int maxValue=-1234567;
    int minValue=12345679;
    int i;
    for(i=0;i<len;i++)
    {
        maxValue=max(maxValue,arr[i]);
        minValue=min(minValue,arr[i]);
    }
    int bucketCount=(maxValue-minValue)/len+1;
    int **buckets=(int**)malloc(sizeof(int*)*bucketCount);
    int *bucketSize=(int*)malloc(sizeof(int)*bucketCount);
    int *bucketCap=(int*)malloc(sizeof(int)*bucketCount);
    memset(bucketSize,0,sizeof(int)*bucketCount);
    for(i=0;i<bucketCount;i++)
    {
        bucketCap[i]=1;
        buckets[i]=(int*)malloc(sizeof(int));
    }
    for(i=0;i<len;i++)
    {
        int bucketId=(arr[i]-minValue)/len;
        if(bucketSize[bucketId]==bucketCap[bucketId])
        {
            bucketCap[bucketId]*=2;
            buckets[bucketId]=realloc(buckets[bucketId],sizeof(int)*bucketCap[bucketId]);
        }
        buckets[bucketId][bucketSize[bucketId]++]=arr[i];
    }
    int outPtr=0;
    int j;
    for(i=0;i<bucketCount;i++)
    {
        subSort(buckets[i],bucketSize[i]);
        for(j=0;j<bucketSize[i];j++)
            arr[outPtr++]=buckets[i][j];
        free(buckets[i]);
    }
    free(bucketSize);
    free(bucketCap);
    free(buckets);
}
    
int main()
{
    int array[]={1,100,1,1,55,56,1,1,1,1};
    int len=sizeof(array)/sizeof(int);
    bucketSort(array,len,quickSort);
    print_int_star(array,len);
    return 0;
}
