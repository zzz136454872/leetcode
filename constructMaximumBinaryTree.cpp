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

void print(vector<bool> a)
{
    for(int i=0;i<(int)a.size();i++)
    {
        cout<<i<<" ";
        if(a[i])
            cout<<"true ";
        else
            cout<<"false ";
    }
    cout<<endl;
}

void print(bool a[],int len)
{
    for(int i=0;i<len;i++)
    {
        cout<<i<<" ";
        if(a[i])
            cout<<"true ";
        else
            cout<<"false ";
    }
    cout<<endl;
}

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

class TreeNode
{
public:
    TreeNode(int x)
    {
        this->x=x;
        this->left=NULL;
        this->right=NULL;
    }
    TreeNode *left,*right;
    int x;
};

#ifndef testMod
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        this->nums=nums;
        return buildTree(0,(int)nums.size()-1);
    }
    
    TreeNode* buildTree(int start,int end)
    {
        if(end<start)
            return NULL;
        //cout<<start<<" "<<end<<endl;
        int max=-1234;
        int i;
        int loc;
        for(i=start;i<=end;i++)
        {
            if(nums[i]>max)
            {
                max=nums[i];
                loc=i;
            }
        }
        //cout<<"max"<<max<<" loc"<<loc<<endl;
        TreeNode* pt=new TreeNode(nums[loc]);
        pt->left=buildTree(start,loc-1);
        pt->right=buildTree(loc+1,end);
        return pt;
    }
       
private:
    vector<int> nums;
};



#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<int> in={3,2,1,6,0,5};
    TreeNode *out=sl.constructMaximumBinaryTree(in);
    cout<<out->left->x<<endl;
    cout<<"finish"<<endl;
#endif 
    return 0;
}

