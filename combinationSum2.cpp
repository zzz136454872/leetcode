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

void print(vector<string> a)
{
    for(int i=0;i<(int)a.size();i++)
        cout<<a[i]<<endl;
}

void print(vector<vector<string>> a)
{
    for(int i=0;i<(int)a.size();i++)
    {
        print(a[i]);
        cout<<endl;
    }
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
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        for(int i=0;i<(int)candidates.size();i++)
        {
            if(i==0||candidates[i]!=candidates[i-1])
            {
                log[candidates[i]]=1;
                candi1.push_back(candidates[i]);
            } else {
                log[candidates[i]]++;
            }
        }
        //print(log);
        print(candi1);
        return cs(target, 0);
    }        

    vector<vector<int>> cs(int target, int minLoc) {
        //cout<<"in: "<<target<<": "<<minLoc<<endl;
        vector<vector<int>> out;
        int j;
        for(int i=minLoc;i<(int)candi1.size();i++)
        {
            j=1;
            while(j<=log[candi1[i]]&&target>=j*candi1[i])
            {
                if(target>j*candi1[i])
                {
                    vector<vector<int>> tmp=cs(target-j*candi1[i],i+1);
                    for(auto a:tmp)
                    {
                        for(int k=0;k<j;k++)
                            a.push_back(candi1[i]);
                        out.push_back(a);
                    }
                }
                else if(target==j*candi1[i])
                {
                    vector<int> tmp(j,candi1[i]);
                    out.push_back(tmp);
                }
                j+=1;
            }
        }
        //cout<<"out: "<<target<<": "<<minLoc<<endl;
        //print(out);
        return out;
    }

private:
    map<int, int> log;
    vector<int> candi1;
};

#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<int> candidates = {10,1,2,7,6,1,5};
    int target = 8;
    vector<vector<int>> out=sl.combinationSum2(candidates,target);
    print(out);
    cout<<out.size()<<endl;
#endif 
    return 0;
}

