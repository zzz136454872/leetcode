/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include"ctools.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//#define testMod
#ifdef testMod
void test() 
{

}
#endif

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

#ifndef testMod
bool uniqueOccurrences(int* arr, int arrSize){
    int count1[2001]={0};
    int count2[1001]={0};
    int i;
    for(i=0;i<arrSize;i++)
        count1[arr[i]+1000]++;
    for(i=0;i<2001;i++)
        count2[count1[i]]++;
    for(i=1;i<1001;i++)
    {
        if(count2[i]>1)
        {
            //printf("%d %d\n",i,count2[i]);
            return false;
        }
    }
    return true;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int arr[] = {1,2};//,2,1,1,3};
    int size=sizeof(arr)/sizeof(int);
    printf("%d\n",uniqueOccurrences(arr,size));
#endif
    return 0;
}
    
