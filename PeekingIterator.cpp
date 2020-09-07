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

void print(vector<string> a)
{
    for(int i=0;i<(int)a.size();i++)
        cout<<a[i]<<endl;
}

void print(vector<vector<string>> a)
{
    for(int i=0;i<(int)a.size();i++)
    {
        print(a[i]);
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

/*
 * Below is the interface for Iterator, which is already defined for you.
 * **DO NOT** modify the interface for Iterator.
 *
 *  class Iterator {
 *		struct Data;
 * 		Data* data;
 *		Iterator(const vector<int>& nums);
 * 		Iterator(const Iterator& iter);
 *
 * 		// Returns the next element in the iteration.
 *		int next();
 *
 *		// Returns true if the iteration has more elements.
 *		bool hasNext() const;
 *	};
 */

class PeekingIterator : public Iterator {
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
        tmp=0;
        peeked=false;
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        if(peeked)
            return tmp;
        peeked=true;
        tmp=Iterator::next();
        return tmp;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
        if(peeked)
        {
            peeked=false;
            return tmp;
        }
        return Iterator::next();
	}
	
	bool hasNext() const {
        return Iterator::hasNext() || peeked;
	}

private:
    int tmp;
    bool peeked;
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

