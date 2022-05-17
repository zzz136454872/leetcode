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
int mem[128];

bool gt(char* w1,char* w2) {
    int i=0;
    while(w1[i]!=0&&w2[i]!=0) {
        int tmp=mem[(long)w1[i]]-mem[(long)w2[i]];
        if(tmp<0)
            return false;
        else if(tmp>0)
            return true;
        i++;
    }
    return w1[i]!=0;
}

bool isAlienSorted(char ** words, int wordsSize, char * order) {
    int i;
    for(i=0;i<26;i++)
        mem[(long)order[i]]=i;
    for(i=0;i<wordsSize-1;i++) {
        if(gt(words[i],words[i+1]))
            return false;
    }
    return true;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int wordsSize=2;
    // char words[][9] = {"hello","leetcode"};
    // char* order = "hlabcdefgijkmnopqrstuvwxyz";
    char words[][9] = {"word","world","row"};
    char* order = "worldabcefghijkmnpqstuvxyz";
    char** w=malloc_char_2star((char*)words,wordsSize,9);
    printf("%d\n",isAlienSorted(w,wordsSize,order));
#endif
    return 0;
}
