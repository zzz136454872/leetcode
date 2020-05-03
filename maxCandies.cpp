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
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        vector<int> visited(status.size());
        vector<int> haveBox(status.size());
        int sum=0;
        for(int i=0;i<(int)initialBoxes.size();i++)
        {
            if(visited[initialBoxes[i]]==0&&status[initialBoxes[i]==1])
            {
                sum+=visit(initialBoxes[i],status,candies,keys,containedBoxes,haveBox,visited);
            }
        }
        return sum;
    }

    int visit(int index,vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& haveBox,vector<int> visited)
    {
        visited[index]=1;
        int sum=candies[index];
        for(int i=0;i<(int)keys[index].size();i++)
        {
            status[keys[index][i]]=1;
            if(visited[status[i]]==0&&
               haveBox[status[i]]==1)
            {
                sum+=candies[status[i]];
                visited[status[i]]=1;
            }
        }

        for(int i=0;i<(int)containedBoxes[index].size();i++)
        {
            haveBox[containedBoxes[index][i]]=1;
            if(visited[containedBoxes[index][i]]==0&&
               status[containedBoxes[index][i]]==1)
            {
                sum+=visit(containedBoxes[index][i],status,candies,keys,containedBoxes,haveBox,visited);
                visited[containedBoxes[index][i]]=1;
            }
        }
        return sum;
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

