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
bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
    if(n==0)
        return true;
    if(flowerbedSize==1)
        return flowerbed[0]==0;
    if(flowerbed[0]==0&&flowerbed[1]==0)
    {
        n--;
        flowerbed[0]=1;
    }
    if(flowerbed[flowerbedSize-1]==0&&flowerbed[flowerbedSize-2]==0)
    {
        n--;
        flowerbed[flowerbedSize-1]=1;
    }
    for(int i=1;i<flowerbedSize-1;i++)
    {
        if(flowerbed[i-1]==0&&flowerbed[i]==0&&flowerbed[i+1]==0)
        {
            n--;
            flowerbed[i]=1;
        }
    }
    return n<=0;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int flowerbed[] = {1,0,0,0,1};
    int n = 2;
    int flowerbedSize=sizeof(flowerbed)/sizeof(int);
    printf("%d\n",canPlaceFlowers(flowerbed,flowerbedSize,n));
#endif
    return 0;
}
    
