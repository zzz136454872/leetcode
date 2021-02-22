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
#include<set>

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
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        for(int i=1;i<(int)matrix.size();i++)
        {
            for(int j=1;j<(int)matrix[0].size();j++)
            {
                if(matrix[i][j]!=matrix[i-1][j-1])
                    return false;
            }
        }
        return true;
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
    vector<vector<int>> matrix = {{1,2,3,4},{5,1,2,3},{9,5,1,2}};
    cout<<sl.isToeplitzMatrix(matrix)<<endl;
#endif 
    return 0;
}

