/* @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{
    vector<vector<string>> s;
    vector<string> tmp;
    tmp.push_back("test");
    s.push_back(tmp);
    tmp.pop_back();
    tmp.push_back("test1");
    s.push_back(tmp);
    for(unsigned long long i=0;i<s.size();i++)
        for(unsigned long long j=0;j<s[i].size();j++)
            cout<<i<<" "<<j<<" "<<s[i][j]<<endl;
    
}
#endif

#ifndef testMod

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> out;
        vector<vector<string>> tmp;
        vector<string>s1;
        s1.push_back("");
        tmp.push_back(s1);
        s1.pop_back();
        s1.push_back("()");
        tmp.push_back(s1);
        string s;
        for(unsigned long long i=2;i<(long long unsigned)(n+1);i++)
        {
            vector<string> test;
            for(unsigned long long j=0;j<i;j++)
            {
                for(unsigned long long k=0;k<tmp[j].size();k++)
                {
                    for(unsigned long long h=0;h<tmp[i-1-j].size();h++)
                    {
                        s="("+tmp[j][k]+")"+tmp[i-1-j][h];
                        test.push_back(s);
                    }
                }
                //for(unsigned long long k=0;i<tmp[j].size();k++)
                //{
                //    for(unsigned long long h=0;h<tmp[i-1-j].size();h++)
                //    {
                //        s=tmp[j][k]+"()";
                //        tmp[i-1].push_back(s);
                //}
            }
            tmp.push_back(test);
        }
        return tmp[n];
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
    vector<string> out=sl.generateParenthesis(3);
    for(unsigned long long j=0;j<out.size();j++)
        cout<<j<<" "<<out[j]<<endl;
#endif 
    return 0;
}

