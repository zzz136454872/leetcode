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
int countPrimes(int n) {
    if(n<=2)
        return 0;
    char* log=(char*)malloc((n+1));
    memset(log,1,n+1);
    log[0]=0;
    log[1]=0;
    long long i,j;
    long long now;
    long long out=0;
    for(i=0;i<n;i++)
    {
        if(log[i])
        {
            //printf("%d %d\n",i,out);
            out++;
            j=i;
            now=i;
            while(j*now<n+1)
                log[(j++)*now]=0;
            //printmem(log,n+1);
        }
    }
    free(log);
    return (int)out;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    printf("%d\n",countPrimes(1));
#endif
    return 0;
}
    
