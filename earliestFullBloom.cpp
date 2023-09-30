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
#include<numeric>

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
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
        vector<pair<int,int>> arr;
        for(int i=0;i<int(plantTime.size());i++) {
            arr.push_back({plantTime[i],growTime[i]});
        }
        sort(arr.begin(),arr.end(), [](pair<int,int>& a, pair<int,int>& b) {
                return a.second>b.second;
            });
        int res=0;
        int total=0;
        for(int i=0;i<int(arr.size());i++) {
            total+=arr[i].first;
            res=max(res,total+arr[i].second);
        }
        return res;
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
    vector<int> plantTime = {1,2,3,2};
    vector<int> growTime = {2,1,2,1};
    cout<<Solution().earliestFullBloom(plantTime,growTime)<<endl;
#endif 
    return 0;
}

