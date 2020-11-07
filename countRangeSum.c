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
int low;
int up;
int mergeCount(long long* nums,int left, int right)
{
    if(left>=right)
        return 0;
    int mid=(left+right)/2;
    int out=mergeCount(nums,left,mid)+mergeCount(nums,mid+1,right);
    int i=left;
    int j=mid+1,k=mid+1;
    while(i<=mid)
    {
        while(j<=right&&nums[j]-nums[i]<low)
            j++;
        while(k<=right&&nums[k]-nums[i]<=up)
            k++;
        out+=k-j;
        i++;
    }
    long long* buffer=(long long*)malloc(sizeof(long long)*(right-left+1));
    i=left;
    j=mid+1;
    k=0;
    while(i<=mid&&j<=right)
    {
        if(nums[i]<nums[j])
            buffer[k++]=nums[i++];
        else
            buffer[k++]=nums[j++];
    }
    while(i<=mid)
        buffer[k++]=nums[i++];
    while(j<=right)
        buffer[k++]=nums[j++];
    memcpy(nums+left,buffer,sizeof(long long)*(right-left+1));
    //printf("left:%d right:%d out:%d\n",left,right,out);
    free(buffer);
    return out;
}

int countRangeSum(int* nums, int numsSize, int lower, int upper){
    low=lower;
    up=upper;
    long long* preSum=(long long*)malloc(sizeof(long long)*(numsSize+1));
    preSum[0]=0;
    for(int i=1;i<numsSize+1;i++)
        preSum[i]=preSum[i-1]+nums[i-1];
    int out=mergeCount(preSum,0,numsSize);
    free(preSum);
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int nums[] = {-2,5,-1};
    //int len=sizeof(nums)/sizeof(int);
    int len=3;
    int lower=-2;
    int upper=2;
    printf("%d\n",countRangeSum(nums,len,lower, upper));
#endif
    return 0;
}
    
