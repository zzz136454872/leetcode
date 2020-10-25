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
int longestMountain(int* A, int ASize){
    int *left=(int*)malloc(sizeof(int)*ASize);
    int *right=(int*)malloc(sizeof(int)*ASize);
    memset(left,0,sizeof(int)*ASize);
    memset(right,0,sizeof(int)*ASize);
    int i;
    for(i=1;i<ASize;i++)
    {
        if(A[i]>A[i-1])
            left[i]=left[i-1]+1;
        else
            left[i]=0;
    }
    for(i=ASize-2;i>=0;i--)
    {
        if(A[i]>A[i+1])
            right[i]=right[i+1]+1;
        else
            right[i]=0;
    }
    int out=0;
    for(i=0;i<ASize;i++)
        out=max(out,left[i]+right[i]+1);
    return out>=3?out:0;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    //int A[]={2,1,4,7,3,2,5};
    int A[]={2,2,2};
    int ASize=sizeof(A)/sizeof(int);
    printf("%d\n",longestMountain(A,ASize));
#endif
    return 0;
}
    
