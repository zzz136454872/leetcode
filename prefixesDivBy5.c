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
bool* prefixesDivBy5(int* A, int ASize, int* returnSize){
    bool* out=(bool*)malloc(sizeof(bool)*ASize);
    *returnSize=ASize;
    int tmp=0;
    for(int i=0;i<ASize;i++)
    {
        tmp=((tmp<<1)+A[i])%5;
        out[i]=(tmp%5==0);
    }
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int inp[]={1,1,1,0,1};
    int size=sizeof(inp)/sizeof(int);
    int retSize;
    bool* out=prefixesDivBy5(inp,size,&retSize);
    print_int_star(out, retSize);
#endif
    return 0;
}
    
