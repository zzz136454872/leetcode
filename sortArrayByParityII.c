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
int* sortArrayByParityII(int* A, int ASize, int* returnSize){
    int i=0,odd=1,even=0;
    int *out=(int*)malloc(sizeof(int)*ASize);
    for(i=0;i<ASize;i++)
    {
        if(A[i]%2==0)
        {
            out[even]=A[i];
            even+=2;
        }
        else
        {
            out[odd]=A[i];
            odd+=2;
        }
    }
    *returnSize=ASize;
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int A[]={4,2,5,7};
    int ASize=sizeof(A)/sizeof(int);
    int returnSize;
    int*out=sortArrayByParityII(A,ASize,&returnSize);
    print_int_star(out,returnSize);
#endif
    return 0;
}
    
