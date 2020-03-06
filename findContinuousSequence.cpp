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
    vector<vector<int>> findContinuousSequence(int target) {
        vector<vector<int>> out;
        vector<int> tmp;
        int sum=0;
        int t=1;
        if(target < 3)
            return out;
        while(t < target/2+3)
        {
            print(tmp);
            cout<<"t="<<t<<endl;
            if(sum==target)
            {
                out.push_back(tmp);
                sum-=tmp[0];
                tmp.erase(tmp.begin());
                cout<<"push"<<endl;
            }
            else if(sum < target)
            {
                sum+=t;
                tmp.push_back(t);
                t++;
            }
            else
            {
                sum-=tmp[0];
                tmp.erase(tmp.begin());
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
    vector<vector<int>> out=sl.findContinuousSequence(15);
    print(out);
#endif 
    return 0;
}

