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
// your code here
int repeatedNTimes(int* nums, int numsSize){
    int tmp[2]={-1,-1};
    int idx=0;
    for(int i=0;i<numsSize;i++) {
        if(tmp[0]==nums[i])
            return nums[i];
        if(tmp[1]==nums[i])
            return nums[i];
        tmp[idx]=nums[i];
        idx^=1;
    }
    return nums[0];
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod

#endif
    return 0;
}
    
