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
        this->status=status;
        this->candies=candies;
        this->keys=keys;
        this->containedBoxes=containedBoxes;
        n=(int)status.size();
        this->visited=vector<bool>(n,false);
        this->haveBox=vector<bool>(n,false);
        candieCount=0;
        for(int b:initialBoxes)
        {
            haveBox[b]=true;
            if(!visited[b])
                visit(b);
        }
        return candieCount;
    }
    
private:
    void visit(int box)
    {
        visited[box]=true;
        candieCount+=candies[box];
        for(vector<int> &newKeys:keys)
        {
            for(int newKey:newKeys)
            {
                status[newKey]=1;
                if(!visited[newKey]&&haveBox[newKey])
                    visit(newKey);
            }
        }
        for(vector<int> &newBoxes:containedBoxes)
        {
            for(int newBox:newBoxes)
            {
                haveBox[newBox]=true;
                if(!visited[newBox]&&status[newBox]==1)
                    visit(newBox);
            }
        }
    }

    vector<int> status;
    vector<int> candies;
    vector<vector<int>> keys;
    vector<vector<int>> containedBoxes;
    vector<bool> visited;
    vector<bool> haveBox;
    int n;
    int candieCount;
};

#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<int> status = {1,0,1,0};
    vector<int> candies = {7,5,4,100};
    vector<vector<int>> keys = {{},{},{1},{}};
    vector<vector<int>> containedBoxes = {{1,2},{3},{},{}};
    vector<int> initialBoxes = {0};
    cout<<sl.maxCandies(status,candies,keys,containedBoxes,initialBoxes)<<endl;
    
#endif 
    return 0;
}

