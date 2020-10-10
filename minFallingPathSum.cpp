/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */
#include"cpptools.h"
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
//下降路径最小和 
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& A) {
        int n=(int)A.size();
        vector<vector<int>> table=vector<vector<int>>(n,vector<int>(n,0));
        for(int j=0;j<n;j++)
            table[0][j]=A[0][j];
        int tmp=12345;
        for(int i=1;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                tmp=123456;
                if(j>0)
                    tmp=min(tmp,table[i-1][j-1]);
                tmp=min(tmp,table[i-1][j]);
                if(j<n-1)
                    tmp=min(tmp,table[i-1][j+1]);
                table[i][j]=tmp+A[i][j];
            }
        }
        tmp=123456;
        for(int j=0;j<n;j++)
            tmp=min(tmp,table[n-1][j]);
        return tmp;
    }
private:
};

//下降路径最小和II
class Solution2 {
public:
    int minFallingPathSum(vector<vector<int>>& arr) {
        int n=(int)arr.size();
        vector<vector<int>> table=vector<vector<int>>(n,vector<int>(n,0));
        for(int j=0;j<n;j++)
            table[0][j]=arr[0][j];
        int tmp=12345;
        for(int i=1;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                tmp=123456;
                for(int k=0;k<n;k++)
                {
                    if(k==j)
                        continue;
                    tmp=min(tmp, table[i-1][k]);
                }
                table[i][j]=tmp+arr[i][j];
            }
        }
        tmp=123456;
        for(int j=0;j<n;j++)
            tmp=min(tmp,table[n-1][j]);
        return tmp;
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
    vector<vector<int>> arr = {{1,2,3},{4,5,6},{7,8,9}};
    cout<<sl.minFallingPathSum(arr)<<endl;
#endif 
    return 0;
}

