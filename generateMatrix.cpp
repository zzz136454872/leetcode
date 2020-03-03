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

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod

class Solution {
public:
    vector<vector<int>> generateMatrix(int n)
    {
        vector<vector<int>> log;
        if(n==0)
            return log;
        

        vector<int> tmp;
        for(int i=0;i<n;i++)
            tmp.push_back(0);
        for(int i=0;i<n;i++)
            log.push_back(tmp);
        int direction=1;
        int i=0,j=0;
        int count=0;
        
        while(true)
        {
            if(log[i][j])
                break;
            log[i][j]=++count;
            if(n==1)
                return log;
            switch(direction)
            {
                case 1:
                    if(j<n-1&&!log[i][j+1])
                        j++;
                    else 
                    {
                        i++;
                        direction++;
                    }
                    break;
                case 2:
                    if(i<n-1&&!log[i+1][j])
                        i++;
                    else 
                    {
                        j--;
                        direction++;
                    }
                    break;
                case 3:
                    if(j>0&&!log[i][j-1])
                        j--;
                    else
                    {
                        i--;
                        direction++;
                    }
                    break;
                case 4:
                    if(i>0&&!log[i-1][j])
                        i--;
                    else
                    {
                        j++;
                        direction=1;
                    }
                    break;
                default:
                    cout<<"error"<<endl;
            }
        }
        return log;
    }

private:
    void print(vector<int> a)
    {
        for(int i=0;i<(int)a.size();i++)
            cout<<a[i]<<" ";
        cout<<endl;
    }

};
#endif

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

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<vector<int>> in= sl.generateMatrix(2);
    print(in);
#endif 
    return 0;
}


