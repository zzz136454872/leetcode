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
#include<windows.h>

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

void print(vector<vector<char>> a)
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
    void solveSudoku(vector<vector<char>>& board) {
        this->board=board;
        solve(0,-1);
        board=this->board;
    }

    bool solve(int i,int j)
    {
        //cout<<i<<j<<endl;
        if(!checkHori(i))
            return false;
        if(!checkVert(j))
            return false;
        if(!checkPart(i/3,j/3))
            return false;
        if(i==8&&j==8)
        {
            return true;
        }
        next(i,j);
        if(board[i][j]=='.')
        {
            for(int h=1;h<10;h++)
            {
                board[i][j]=h+'0';
                if(solve(i,j))
                {
                    return true;
                }
            }           
            board[i][j]='.';
        }
        else
        {
            if(solve(i,j))
            {
                return true;
            }
        }
        last(i,j);
        return false;
    }

    void next(int &i,int &j)
    {
        if(j<8)
        {
            j++;
            return;
        }
        else
        {
            if(i<8)
            {
                i++;
                j=0;
                return;
            }
            else
                cout<<"error"<<endl;
        }
    }

    void last(int &i,int &j)
    {
        if(j>0)
        {
            j--;
            return;
        }
        else
        {
            if(i>0)
            {
                j=8;
                i--;
            }
            else
                cout<<"error in last"<<endl;
        }
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
        if(j==-1)
            return true;
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
    
    sl.solveSudoku(in);
    print(in);

#endif 
    return 0;
}

