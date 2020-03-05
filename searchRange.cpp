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

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> out;
        
        if(nums.size()==0||nums[0]>target||nums[nums.size()-1]<target)
        {
            out.push_back(-1);
            out.push_back(-1);
            return out;
        }

        int start=-1;
        int end=-1;
        int mid;
        //cout<<"flag"<<endl;
        if(nums[0]==target)
            start=0;
        else
        {
            int tmps=0;
            int tmpe=nums.size()-1;
            while(tmps<tmpe)
            {
                mid=(tmps+tmpe)/2;
                if(nums[mid]<target)
                    tmps=mid+1;
                else 
                    tmpe=mid;
            }
            if(nums[tmps]==target)
                start=tmps;
            else
                start=-1;
        }
        //cout<<"flag"<<endl;
        if(nums[nums.size()-1]==target)
            end=nums.size()-1;
        else
        {
            int tmps=0;
            int tmpe=nums.size()-1;
            while(tmps<tmpe)
            {
                //cout<<tmps<<" "<<tmpe<<endl;
                mid=(tmps+tmpe+1)/2;
                if(nums[mid] > target)
                    tmpe=mid-1;
                else
                    tmps=mid;
            }
            if(nums[tmpe]==target)
                end=tmpe;
            else
                end=-1;
        }
        //cout<<"flag"<<endl;
        out.push_back(start);
        out.push_back(end);
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
    vector<int> nums = {5,7,7,8,8,10};
    int target = 8;
    vector<int> out=sl.searchRange(nums,target);
    print(out); 
    
#endif 
    return 0;
}

