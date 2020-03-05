#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

//#define test

#ifdef test
void testFunc()
{
    int t=-1;
    cout<<abs(t)<<endl;
}
#endif

bool cmp(int a,int b)
{
    return a < b; //升序
}

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(begin(nums),end(nums),cmp);
        int high,low;
        int tmp;
        int sum=1<<25;
        
        for(unsigned long long i=0;i<nums.size()-2;i++)
        {
            low=i+1;
            high=nums.size()-1;
            while(low<high)
            {
                tmp=nums[high]+nums[low]+nums[i];
                if(abs(tmp-target) < abs(sum-target))
                    sum=tmp;
                if(tmp < target)
                    low++;
                else
                    high--;
            }
        }
        return sum;
    }
};

int main()
{
#ifdef test
    testFunc();
#endif
    Solution sl;
    vector<int> in = {-1,2,1,-4};
    int out = sl.threeSumClosest(in,1);
    cout<<out<<endl;
    return 0;
}


