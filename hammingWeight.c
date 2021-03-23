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
int hammingWeight(int n) {
    int out=0;
    while(n!=0)
    {
        n&=(n-1);
        printf("%d\n",n);
        out++;
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
    printf("%d\n",hammingWeight(-1));
#endif
    return 0;
}
    
