/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */
#include"cpptools.h"
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{

    
}
#endif

#ifndef testMod
class Solution {
public:
    int longestPalindrome(string word1, string word2) {
        return longestPalindromeSubseq(word1+word2);
    }

    int longestPalindromeSubseq(string s) {
        if(s.size()==0)
            return 0;
        table=vector<vector<int>>(s.size(),vector<int>(s.size(),0));
        this->s=s;
        return find(0,(int)s.size()-1);
    }

    int find(int begin,int end)
    {
        if(begin>end)
            return 0;
        if(begin==end)
            return 1;
        if(table[begin][end]!=0)
            return table[begin][end];
        int maxLen=max(find(begin+1,end),find(begin,end-1));
        if(s[begin]==s[end])
            maxLen=max(maxLen,find(begin+1,end-1)+2);
        table[begin][end]=maxLen;
        return maxLen;
    }

private:
    vector<vector<int>> table;
    string s;
};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    string word1 = "aa";
    string word2 = "bb";
    cout<<sl.longestPalindrome(word1,word2)<<endl;
#endif 
    return 0;
}

