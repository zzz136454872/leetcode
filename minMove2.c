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
int cmp(const void* a, const void*b) {
    return *(int*)a-*(int*)b;
}

int sub_abs(int a,int b) {
    return a>b?a-b:b-a;
}

// your code here
int minMoves2(int* nums, int numsSize){
    qsort(nums,numsSize,sizeof(int),cmp);
    int mid=nums[numsSize/2];
    int res=0;
    for(int i=0;i<numsSize;i++) {
        res+=sub_abs(nums[i],mid);
    }
    return res;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    // int nums[] = {1,2,3};
    int nums[] = {1,10,2,9};
    int length=sizeof(nums)/sizeof(int);
    printf("%d\n",minMoves2(nums,length));
#endif
    return 0;
}
    
