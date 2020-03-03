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

#ifndef testMod

class Solution {
public:
    
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        int loc=0;
        while(loc<n)
        {
            A[m+loc]=B[loc];
            loc++;
        }
        sort(A.begin(),A.end());
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

    vector<int> a,b;
    // 1,2,3,0,0,0
    // 2,5,6
    a.push_back(1);
    a.push_back(2);
    a.push_back(3);
    for(int i=0;i<3;i++)
        a.push_back(0);
    b.push_back(2);
    b.push_back(5);
    b.push_back(6);
    sl.merge(a,3,b,3);
    
    for(unsigned long long i=0;i<a.size();i++)
        cout<<a[i]<<endl;
    


    
#endif 
    return 0;
}

