/* @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod

class Solution {
private:


public:
    int strStr(string haystack, string needle) {
        if(needle.size() ==0)
            return 0;
        if(haystack.size()<needle.size())
            return -1;
       
        for(unsigned long long i=0;i<haystack.size();i++)
        {
            unsigned long long j;
            bool right=true;
            for(j=0;j<needle.size();j++)
            {
                if(i+j >= haystack.size())
                    return -1;
                if(haystack[i+j]!=needle[j])
                {
                    right=false;
                    break;
                }
            }
            if(right)
                return i;
        }
        return -1;
    }
};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    string haystack = "abababc",needle = "ababc";
    int test=sl.strStr(haystack,needle);
    cout<<"test: "<<test<<endl;

#endif 
    return 0;
}

