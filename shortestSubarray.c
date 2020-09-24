/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

// wrong answer

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
int shortestSubarray(int* A, int ASize, int K){
    int begin,end;
    begin=0;
    end=0;
    int sum=0;
    int minLen=123456;
    while(end<ASize||sum>=K)
    {
        printf("%d %d %d %d\n",begin,end,sum,minLen);
        if(sum<0)
        {
            begin=end;
            sum=0;
        }
        else if(sum<K)
        {
            sum+=A[end++];
        }
        else if(sum>=K)
        {
            minLen=min(minLen,end-begin);
            sum-=A[begin++];
        }
    }
    return minLen>12345?-1:minLen;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int A[] = {84,-37,32,40,95};
    int K = 167;
    int len=sizeof(A)/sizeof(int);
    printf("%d\n",shortestSubarray(A,len,K));
#endif
    return 0;
}
    
