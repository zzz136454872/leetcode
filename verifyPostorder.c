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

int verifySub(int* postorder,int start,int end)
{
    //printf("%d, %d\n",start,end);
    if(start>=end)
        return true;
    int mid=start;
    while(mid<end&&postorder[mid]<postorder[end])
        mid++;
    for(int i=mid;i<end;i++)
    {
        if(postorder[i]<postorder[end])
            return false;
    }
    return verifySub(postorder,start,mid-1)&&verifySub(postorder,mid,end-1);
}

int verifyPostorder(int* postorder, int postorderSize){
    return verifySub(postorder, 0, postorderSize-1); 
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    //int nums[]={1,2,5,10,6,9,4,3};
    int nums[]={6,7};
    int len=sizeof(nums)/sizeof(int);
    printf("%d\n",(int)verifyPostorder(nums,len));
#endif
    return 0;
}
    
