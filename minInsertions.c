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

#ifndef testMod


#define min(a,b) (((a)<(b))?(a):(b))

int table[1000][1000];
char* str;

int minInsertionsSub(int a, int b)
{
    if(a>=b)
        return 0;
    if(table[a][b]!=-1)
        return table[a][b];
    int minInsert=123456;
    if(str[a]==str[b])
        minInsert=min(minInsertionsSub(a+1,b-1),minInsert);
    else
        minInsert=min(minInsertionsSub(a,b-1),minInsertionsSub(a+1,b))+1;
    table[a][b]=minInsert;
    return minInsert;
}

int minInsertions(char * s){
    str=s;
    for(int i=0;i<1000;i++)
    {
        for(int j=0;j<1000;j++)
            table[i][j]=-1;
    }
    return minInsertionsSub(0,strlen(s)-1);
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    char* s = "leetcode";
    printf("%d\n",minInsertions(s));
#endif
    return 0;
}
    
