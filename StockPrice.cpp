#include"cpptools.h"
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>
#include<set>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod
typedef struct {
    int price;
    int time;
} Node;

class StockPrice {
public:
    StockPrice() {
        s1=priority_queue<Node,vector<Node>,[](Node& a,Node& b) {
                return a.price<b.price;
                }>();
    }
    
    void update(int timestamp, int price) {

    }
    
    int current() {

    }
    
    int maximum() {

    }
    
    int minimum() {

    }
private:
    priority_queue<Node> s1;
    priority_queue<Node> s2;
    map<int,int> prices;
    int latest=0;
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

