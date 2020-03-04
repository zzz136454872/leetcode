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

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod
class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> out;
        for(int i=0;i<(int)num_people;i++)
            out.push_back(0);
        int loc=0;
        int count=1;
        while(true)
        {
            if(candies>=count)
            {
                candies-=count;
                out[loc]+=count;
            }
            else
            {
                out[loc]+=candies;
                return out;
            }
            loc=(loc+1)%num_people;
            count++;
        }
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


    
#endif 
    return 0;
}

