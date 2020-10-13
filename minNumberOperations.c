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
int minNumberOperations(int* target, int targetSize){
    if(targetSize==0)
        return 0;
    int out=target[0];
    for(int i=1;i<targetSize;i++)
        out+=max(target[i]-target[i-1],0);
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int target[]={3,1,1,2};
    int targetSize=sizeof(target)/sizeof(int);
    printf("%d\n",minNumberOperations(target,targetSize));
#endif
    return 0;
}
    
