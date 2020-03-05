#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

//#define testMod

bool cmp(int a,int b)
{
    return a < b; //升序
}

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod

class Solution {
private:


public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> out;
        if(nums.size() < 4)
            return out;
        sort(begin(nums),end(nums),cmp);
        int high,low,mid,want;
        for(unsigned long long i=0;i<nums.size()-3;i++)
        {
            if(i!=0&&nums[i]==nums[i-1])
                continue;
            for(unsigned long long j=i+1;j<nums.size()-2;j++)
            {
                if(j!=i+1&&nums[j]==nums[j-1])
                    continue;
                for(unsigned long long k=j+1;k<nums.size()-1;k++)
                {
                    if(k!=j+1&&nums[k]==nums[k-1])
                        continue;
                    cout<<i<<j<<k<<endl;
                    low=k+1;
                    high=nums.size()-1;
                    want=target-nums[i]-nums[j]-nums[k];

                    while(low<=high)
                    {
                        mid=(high+low)/2;
                        cout<<i<<j<<k<<high<<low<<mid<<endl;
                        if(nums[mid]==want)
                        {
                            out.push_back({nums[i],nums[j],nums[k],nums[mid]});
                            break;
                        }
                        else if(nums[mid]<want)
                        {
                            low=mid+1;
                        }
                        else
                        {
                            high=mid-1;
                        }
                    }
                }
            }
        }
        return out;
    }
};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<int> nums ={1, 0, -1, 0, -2, 2};
    int target = 0;
    vector<vector<int>> out = sl.fourSum(nums,target);
    for(unsigned long long i=0;i<out.size();i++)
    {
        for(unsigned long long j=0;j<out[1].size();j++)
        {
            cout<<out[i][j]<<" ";
        }
        cout<<endl;
    }

#endif 
    return 0;
}

