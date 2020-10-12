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
char* s1;
char* s2;
int len1,len2;
int** table;

int longestSub(int x, int y)
{
    //printf("%d %d\n",x,y);
    if(x==len1||y==len2)
        return 0;
    if(table[x][y]!=-1)
        return table[x][y];
    int maxLen=0;
    if(s1[x]==s2[y])
        maxLen=max(maxLen,longestSub(x+1, y+1)+1);
    else
        maxLen=max(longestSub(x+1,y),longestSub(x,y+1));
    table[x][y]=maxLen;
    return maxLen;
}
    
int longestCommonSubsequence(char * text1, char * text2)
{
    s1=text1;
    s2=text2;
    len1=strlen(s1);
    len2=strlen(s2);
    table=(int**)malloc(sizeof(int*)*len1);
    for(int i=0;i<len1;i++)
    {
        table[i]=(int*)malloc(sizeof(int)*len2);
        for(int j=0;j<len2;j++)
            table[i][j]=-1;
    }
    int out=longestSub(0,0);
    for(int i=0;i<len1;i++)
        free(table[i]);
    free(table);
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    char* text1 = "qtkt";
    char* text2 = "qwhe";
    printf("%d\n",longestCommonSubsequence(text1,text2));
#endif
    return 0;
}
    
