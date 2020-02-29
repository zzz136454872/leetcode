
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
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        loc1=loc2=0;
        for(loc2=0;loc2<nums.size();loc2++)
        {
            if(nums[loc2]==nums[loc1])
                continue;
            loc1++;
            nums[loc1]=nums[loc2];
        }
        return loc1+1;
    }
private:
    int loc1,loc2;
};

#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;


    
#endif 
    return 0;
}

