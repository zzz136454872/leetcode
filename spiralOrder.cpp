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
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<vector<bool>> log;
        vector<int> out;
        if(matrix.size()==0)
            return out;
        if(matrix[0].size()==0)
            return out;
        if(matrix.size()==1)
            return matrix[0];

        if(matrix[0].size()==1)
        {
            for(int i=0;i<(int)matrix.size();i++)
                out.push_back(matrix[i][0]);
            return out;
        }

        vector<bool> tmp;
        for(int i=0;i<(int)matrix[0].size();i++)
            tmp.push_back(false);
        for(int i=0;i<(int)matrix.size();i++)
            log.push_back(tmp);

        cout<<"flag"<<endl;

        int direction=1;
        int i=0,j=0;
        while(true)
        {
            if(log[0][3]==false)
                cout<<"true"<<endl;
            cout<<"i: "<<i<<" j: "<<j<<" direction: "<<direction<<endl;
            if(log[i][j])
                break;
            out.push_back(matrix[i][j]);
            log[i][j]=true;
//1 2 3 4 
//5 6 7 8 
//9 10 11 12 
//flag
//i: 0 j: 0 direction: 1
//i: 0 j: 1 direction: 1
//i: 0 j: 2 direction: 1
//i: 1 j: 2 direction: 2
//i: 2 j: 2 direction: 2
//i: 2 j: 1 direction: 3
//i: 2 j: 0 direction: 3
//i: 1 j: 0 direction: 4
//i: 1 j: 1 direction: 1
//i: 2 j: 1 direction: 2
//flag

//i: 0 j: 0 direction: 1
//i: 0 j: 1 direction: 1
//i: 0 j: 2 direction: 1
//j: 2 o.size 4 true 1
//i: 1 j: 2 direction: 2
//i: 2 j: 2 direction: 2
//i: 2 j: 1 direction: 3
//i: 2 j: 0 direction: 3
//i: 1 j: 0 direction: 4
//i: 1 j: 1 direction: 1
//j: 1 o.size 4 true 1
//i: 2 j: 1 direction: 2

            switch(direction)
            {
                case 1:
                    if(j<matrix[0].size()-1&&log[i][j+1]==false)
                        j++;
                    else 
                    {
                        cout<<"j: "<<j<<" o.size "<<matrix[0].size()<<" true "<<(int)log[i][j+1]<<endl;
                        i++;
                        direction++;
                    }
                    break;
                case 2:
                    if(i<matrix.size()-1&&log[i+1][j]==false)
                        i++;
                    else 
                    {
                        j--;
                        direction++;
                    }
                    break;
                case 3:
                    if(j>0&&log[i][j-1]==false)
                        j--;
                    else
                    {
                        i--;
                        direction++;
                    }
                    break;
                case 4:
                    if(i>0&&log[i-1][j]==false)
                        i--;
                    else
                    {
                        j++;
                        direction=1;
                    }
                    break;
                default:
                    cout<<"error"<<endl;
            }
        }
        return out;
    }

private:
    void print(vector<int> a)
    {
        for(int i=0;i<(int)a.size();i++)
            cout<<a[i]<<" ";
        cout<<endl;
    }

};
#endif

void print(vector<int> a)
{
    for(int i=0;i<(int)a.size();i++)
        cout<<a[i]<<" ";
    cout<<endl;
}


int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<vector<int>> in=
       {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
    vector<int> out=sl.spiralOrder(in);
    print(out);

#endif 
    return 0;
}


