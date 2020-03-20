/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>

using namespace std;

//显示中间结果
void print(vector<int> a)
{
    for(int i=0;i<(int)a.size();i++)
        cout<<a[i]<<" ";
    cout<<endl;
}

void print(vector<vector<int>> a)
{
    for(int i=0;i<(int)a.size();i++)
    {
        for(int j=0;j<(int)a[i].size();j++)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }
}

void print(vector<bool> a)
{
    for(int i=0;i<(int)a.size();i++)
    {
        cout<<i<<" ";
        if(a[i])
            cout<<"true ";
        else
            cout<<"false ";
    }
    cout<<endl;
}

void print(bool a[],int len)
{
    for(int i=0;i<len;i++)
    {
        cout<<i<<" ";
        if(a[i])
            cout<<"true ";
        else
            cout<<"false ";
    }
    cout<<endl;
}

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod
class Solution {
public:
    int longestPalindrome(string s) {
        int table[130]={0};
        for(int i=0;i<(int)s.size();i++)
        {
            table[(int)s[i]]++;
        }
        int out=0;
        bool flag=false;
        for(int i=0;i<130;i++)
        {
            if(!flag)
            {
                if(table[i]>0)
                {
                    out+=table[i];
                    if(table[i]%2)
                        flag=true;
                }
            }
            else
            {
                out+=((table[i]>>1)<<1);
            }
        }
        return out;
    }


        
private:
};



#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    string in="abccccdd";
    cout<<sl.longestPalindrome(in)<<endl;


    
#endif 
    return 0;
}

