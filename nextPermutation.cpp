/* @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>

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
    void nextPermutation(vector<int>& nums) {
        if(nums.size() < 2)
          return;
        unsigned long long i;

        for(i=nums.size()-1;i>=1;i--)
        {
            if(i>0&&nums[i] > nums[i-1])
                break;
        }

        int tmp;
        int start=i;
        int end=nums.size()-1;

        while(start<end)
        {
            tmp=nums[start];
            nums[start]=nums[end];
            nums[end]=tmp;
            start++;
            end--;
        }
        unsigned long long j=i;
        if(i==0)
            return;
            
        while(nums[j] <= nums[i-1])
            j++;

        tmp=nums[j];
        nums[j]=nums[i-1];
        nums[i-1]=tmp;
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
    vector<int> in = {1,5,2};
    //vector<int> in={1};
    sl.nextPermutation(in);
    for(unsigned long long i=0;i<in.size();i++)
        cout<<in[i]<<" ";
    cout<<endl;
#endif 
    return 0;
}

