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

#ifndef testMod
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.size()==0)
            return -1;
        
        if(nums.size()==1)
        {
            if(nums[0]==target)
                return 0;
            else
                return -1;
        }
        int start=0;
        int end=nums.size()-1;
        int mid;
        if(nums[0]==target)
            return 0;
        if(nums[nums.size()-1]==target)
            return nums.size()-1;
        if(nums[0]<nums[nums.size()-1])
        {
            while(start<=end)
            {
                mid=(start+end)/2;
                if(nums[mid]==target)
                    return mid;
                if(nums[mid] > target)
                    end=mid-1;
                else
                    start=mid+1;
            }
            return -1;
        }


        while(start<end)
        {
            mid=(start+end)/2;
            if(nums[mid]==target)
                return mid;
            if(nums[mid]<=nums[start])
                end=mid;
            else
                start=mid;
        }
        cout<<"start "<<start<<" end "<<end<<endl;
        if(target > nums[nums.size()-1])
        {
            end=start;
            start=0;
        }
        else
        {
            start=end+1;
            end=nums.size()-1;
        }

        cout<<"start "<<start<<" end "<<end<<endl;
        
        while(start<=end)
        {
            mid=(start+end)/2;
            if(nums[mid]==target)
            {
                return mid;
            }
            if(nums[mid] > target)
                end=mid-1;
            else
                start=mid+1;
        }
        return -1;
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
    vector<int> in={1,3};
    int out=sl.search(in,1);
    cout<<out<<endl;
#endif 
    return 0;
}

