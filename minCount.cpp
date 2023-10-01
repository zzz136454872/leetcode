/**
 * @author f4prime
 * @email zzz136454872@163.com
 */
#include "cpptools.h"
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

//#define testMod

#ifdef testMod
void test() {}
#endif

#ifndef testMod
class Solution {
public:
  int minCount(vector<int> &coins) {
    int res = 0;
    for (int coin : coins) {
      res += (coin + 1) / 2;
    }
    return res;
  }

private:
};
#endif

int main() {
#ifdef testMod
  test();
#endif

#ifndef testMod
  Solution sl;
  vector<int> coins = {4, 2, 1};
  cout << sl.minCount(coins) << endl;
#endif
  return 0;
}
