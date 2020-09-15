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

#ifndef testMOd

int numWaterBottles(int numBottles, int numExchange){
    int out=0;
    int rest=numBottles;
    int k;
    while(rest>=numExchange)
    {
        k=rest/numExchange;
        rest=rest%numExchange;
        out+=k*numExchange;
        rest+=k;
    }
    out+=rest;
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int numBottles = 15, numExchange = 4;
    printf("%d\n", numWaterBottles(numBottles, numExchange));
#endif
    return 0;
}
    
