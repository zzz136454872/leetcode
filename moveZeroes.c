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
void moveZeroes(int* nums, int numsSize){
    int i=0,j=0;
    int tmp;
    while(j<numsSize)
    {
        while(i<numsSize&&nums[i]!=0)
            i++;
        if(i==numsSize)
            break;
        j=max(j,i);
        while(j<numsSize&&nums[j]==0)
            j++;
        if(j==numsSize)
            break;
        tmp=nums[i];
        nums[i]=nums[j];
        nums[j]=tmp;
        //print_int_star(nums,5);
    }
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    //int nums[]={0,1,0,3,12};
    int nums[]={1,1,0,3,12};
    int len=sizeof(nums)/sizeof(int);
    moveZeroes(nums,len);
    print_int_star(nums,len);
#endif
    return 0;
}
    
