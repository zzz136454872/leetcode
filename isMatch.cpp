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

void print(vector<vector<int> > a)
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
    bool isMatch(string s, string p) {
        this->s=s;
        this->p=p;
        return test(0,0);
        //cout<<"ismatch"<<endl;
    }

    bool match(char a, char b)
    {
        //cout<<"match"<<endl;
        if(a == b)
            return true;
        return a=='.';
    }

    bool test(int s_loc,int p_loc)
    {
        //cout<<"test "<<s_loc<<" "<<p_loc<<endl;
        while(s_loc<s.size()&&p_loc<p.size()&&s[s_loc]==p[p_loc])
        {
            s_loc++;
            p_loc++;
        }
        //if(s_loc > 10 || p_loc>10)
        //  exit(0);
        //cout<<"test1 "<<s_loc<<" "<<p_loc<<endl;
        if(s_loc==s.size())
        {
            if(p_loc==p.size())
                return true;
            if(p_loc<p.size()-1&&p[p_loc+1]=='*')
                return test(s_loc,p_loc+2);
        }
        if(p_loc==p.size())
            return false;
        if(p[p_loc]=='.')
            return test(s_loc+1,p_loc+1);
        if(p[p_loc]=='*')
        {
            if(p_loc==0)
                return false;
            if(s_loc>0&&test(s_loc-1,p_loc+1))
                return true;
            if(test(s_loc,p_loc+1))
                return true;
            while(s_loc<s.size()&&match(p[p_loc-1],s[s_loc]))
            {
                if(test(s_loc+1,p_loc+1))
                {
                    return true;
                }
                //cout<<"flag "<<s_loc<<" "<<p_loc<<endl;
                s_loc++;
            }
            return false;
        }
        if(p_loc<p.size()-1&&p[p_loc+1]=='*')
            return test(s_loc,p_loc+2);
        return false;
    }
private:
    string s,p;
};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    string s="aaaaaab";
    string p="a*a*a*a*a*a*c";
    if(sl.isMatch(s,p))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
#endif 
    return 0;
}
