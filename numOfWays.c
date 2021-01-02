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
int numOfWays(int n){
    long long mod=1000000000+7;
    long long *log1=malloc(sizeof(long long)*(n+1));
    long long *log2=malloc(sizeof(long long)*(n+1));
    memset(log1,0,sizeof(long long)*(n+1));
    log1[1]=6;
    log2[1]=6;
    for(int i=2;i<=n;i++)
    {
        log1[i]=(2*log1[i-1]+2*log2[i-1])%mod;
        log2[i]=(2*log1[i-1]+3*log2[i-1])%mod;
    }
    int out=(int)((log1[n]+log2[n])%mod);
    free(log1);
    free(log2);
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int n=5000;
    printf("%d\n", numOfWays(n));
#endif
    return 0;
}
    
