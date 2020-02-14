#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

bool cmp(int a,int b)
{
    return a < b; //升序
}

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(begin(nums),end(nums),cmp);
        int high,low,mid,target;
        for(unsigned long long i=0;i<nums.size()-2;i++)
        {
            if(i!=0&&nums[i]==nums[i-1])
                continue;
            for(unsigned long long j=i+1;j<nums.size()-1;j++)
            {
                if(j!=i+1&&nums[j]==nums[j-1])
                    continue;
                low=j+1;
                high=nums.size();
                target=-1*(nums[i]+nums[j]);
                while(low<=high)
                {
                    mid=(high+low)/2;
                    if(nums[mid]==target)
                    {
                        out.push_back({nums[i],nums[j],nums[mid]});
                        break;
                    }
                    else if(nums[mid]<target)
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
        return out;
    }
};

int main()
{
    Solution sl;

    vector<int> in = {-1, 0, 1, 2, -1, -4};
    vector<int> in2;
    vector<vector<int>> out = sl.threeSum(in);

    for(unsigned long long i=0;i<out.size();i++)
    {
        for(unsigned long long j=0;j<out[1].size();j++)
        {
            cout<<out[i][j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}


