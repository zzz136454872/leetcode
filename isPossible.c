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

#ifndef testMod

// strange error
#define min(a,b) (((a)<(b))?(a):(b))
bool isPossible(int* nums, int numsSize){
    int i=0;
    int s1=0,s2=0,s3=0;
    int previous=-1;
    int now;
    int count;
    int starti;
    while(i<numsSize)
    {
        now=nums[i];
        starti=i;
        while(i<numsSize&&now==nums[i])
            i++;
        count=i-starti;
        if(now-previous>1)
        {
            if(s1!=0||s2!=0)
                return false;
            s1=count;
            s2=0;
            s3=0;
            previous=now;
            continue;
        }
        previous=now;
        if(count<s1+s2)
            return false;
        int rest=count-s1-s2;
        int keep=min(rest, s3);
        s3=keep+s2;
        s2=s1;
        s1=rest-keep;
    }
    return s1==0&&s2==0;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int nums[]={1,2,3,3,4,4,5,5};
    int numsSize=sizeof(nums)/sizeof(int);
    printf("%d\n",isPossible(nums,numsSize));
#endif
    return 0;
}
    
