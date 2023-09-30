#include<iostream>
using namespace std;


class Solution {
public:
    int passThePillow(int n, int time) {
        time=time%(2*n-2);
        if(n>time) {
            return time+1;
        }
        return 2*n-time-1;
    }
};

int main() {
    cout<<"hello world"<<endl;
    Solution sl = Solution();
    cout<<sl.passThePillow(3,2)<<endl;
    return 0;
}
