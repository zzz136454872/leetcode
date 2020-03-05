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
            cout<<"true";
        else
            cout<<"false";
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

#ifndef testMod
class Solution {
public:

    bool isValidSudoku(vector<vector<char>>& board) {
        this->board=board;
        for(int i=0;i<9;i++)
        {
            if(checkHori(i)==false)
                return false;
        }
        for(int j=0;j<9;j++)
        {
            if(checkVert(j)==false)
                return false;
        }
        //cout<<"flag"<<endl;
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                cout<<"i "<<i<<" j "<<j<<endl;
                if(checkPart(i,j)==false)
                    return false;
            }
        }
        //cout<<"flag2"<<endl;
        return true;
    }

    bool checkHori(int i)
    {
        bool table[10]={false};
        for(int h=0;h<9;h++)
        {
            if(board[i][h]=='.')
                continue;
            if(table[(int)board[i][h]-'0'])
                return false;
            table[(int)board[i][h]-'0']=true;
        }
        return true;
    }
    
    bool checkVert(int j)
    {
        bool table[10]={false};
        for(int h=0;h<9;h++)
        {
            if(board[h][j]=='.')
                continue;
            if(table[(int)board[h][j]-'0'])
                return false;
            table[(int)board[h][j]-'0']=true;
        }
        return true;
    }

    bool checkPart(int i, int j)
    {
        bool table[10]={false};
        for(int k=0;k<3;k++)
        {
            for(int h=0;h<3;h++)
            {
                //if(i==1&&j==0)
                //{
                //    cout<<"k "<<k<<" h "<<h<<" board "<<endl;
                //    print(table,10);
                //}
                if(board[3*i+k][3*j+h]=='.')
                    continue;
                if(table[(int)board[3*i+k][3*j+h]-'0'])
                    return false;
                table[(int)board[3*i+k][3*j+h]-'0']=true;
            }
        }
        return true;
    }
        
private:
    vector<vector<char>> board;

};



#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<vector<char>> in=
{
    {'5','3','.','.','7','.','.','.','.'},
    {'6','.','.','1','9','5','.','.','.'},
    {'.','9','8','.','.','.','.','6','.'},
    {'8','.','.','.','6','.','.','.','3'},
    {'4','.','.','8','.','3','.','.','1'},
    {'7','.','.','.','2','.','.','.','6'},
    {'.','6','.','.','.','.','2','8','.'},
    {'.','.','.','4','1','9','.','.','5'},
    {'.','.','.','.','8','.','.','7','9'}
};
    
    bool out=sl.isValidSudoku(in);
    if(out)
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;

#endif 
    return 0;
}

