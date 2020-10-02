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
int letter2num(char letter)
{
    if(letter>='a')
        return letter-'a'+26;
    return letter-'A';
}

int numJewelsInStones(char * J, char * S){
    int set[52]={0};
    for(int i=0;i<strlen(S);i++)
        set[letter2num(S[i])]++;
    int out=0;
    for(int i=0;i<strlen(J);i++)
    {
        out+=set[letter2num(J[i])];
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
    char* J = "aA";
    char* S = "aAAbbbb";
    printf("%d\n",numJewelsInStones(J,S));
#endif
    return 0;
}
    
