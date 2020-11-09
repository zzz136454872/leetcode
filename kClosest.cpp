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
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        vector<vector<int>> log;
        int distance;
        for(int i=0;i<(int)points.size();i++)
        {
            distance=points[i][0]*points[i][0]+points[i][1]*points[i][1];
            log.push_back(vector<int>{distance,points[i][0],points[i][1]});
        }
        sort(log.begin(),log.end());
        vector<vector<int>> out;
        for(int i=0;i<K;i++)
        {
            out.push_back(vector<int>{log[i][1],log[i][2]});
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
    vector<vector<int>> points = {{1,3},{-2,2}};
    int k=1;
    print(sl.kClosest(points,k));
#endif 
    return 0;
}

