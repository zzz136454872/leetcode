/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */
#include"cpptools.h"
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>
#include<set>
#include<cstdlib>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod
class RandomizedCollection {
public:
    /** Initialize your data structure here. */
    RandomizedCollection() {

    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        int index=buffer.size();
        buffer.push_back(val);
        if(dict.find(val)!=dict.end()) 
        {
            dict[val].insert(index);
            return false;
        }
        else 
        {
            dict[val]=set<int>();
            dict[val].insert(index);
	        return true;
        }
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        if(dict.find(val)==dict.end())
            return false;
        if(dict[val].size()==0)
            return false;
        //cout<<"val: "<<val<<" size "<<dict[val].size()<<endl;
        int del_index=*dict[val].begin();
        dict[val].erase(del_index);
        int tmp=*buffer.rbegin();
        buffer.pop_back();
        if(del_index==(int)buffer.size())
            return true;
        int last_index=(int)buffer.size();
        buffer[del_index]=tmp;
        dict[tmp].erase(last_index);
        dict[tmp].insert(del_index);
        return true;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        if(buffer.size()>0)
        {
            int index=rand()%buffer.size();
            return buffer[index];
        }
        return -1;
    }
private:
    map<int,set<int> > dict;
    vector<int> buffer;
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 */
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    RandomizedCollection* obj = new RandomizedCollection();
    bool out1 = obj->insert(0);
    cout<<"out1: "<<out1<<endl;
    out1 = obj->remove(0);
    cout<<"out1: "<<out1<<endl;
    out1 = obj->insert(-1);
    cout<<"out1: "<<out1<<endl;
    out1 = obj->remove(0);
    cout<<"out1: "<<out1<<endl;
    int outInt = obj->getRandom();
    cout<<"outInt: "<<outInt<<endl;
    outInt = obj->getRandom();
    cout<<"outInt: "<<outInt<<endl;
    outInt = obj->getRandom();
    cout<<"outInt: "<<outInt<<endl;
    //out1 = obj->remove(1);
    //cout<<"out1: "<<out1<<endl;
    //outInt = obj->getRandom();
    //cout<<"outInt: "<<outInt<<endl;
    
#endif 
    return 0;
}

