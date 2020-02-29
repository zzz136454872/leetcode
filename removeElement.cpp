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

    int removeElement(vector<int>& nums, int val) {
        if(nums.size() == 0)
            return 0;
        int loc1,loc2;
        loc1=0;
        
        for(loc2=0;loc2<nums.size();loc2++)
        {
            if(nums[loc2]==val)
                continue;
            nums[loc1++]=nums[loc2];
        }
        return loc1;
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


    
#endif 
    return 0;
}

