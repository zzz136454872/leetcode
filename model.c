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
// your code here

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod

#endif
    return 0;
}
    
