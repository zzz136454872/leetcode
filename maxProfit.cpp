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
  int maxProfit(vector<int> &prices) {
    int premin = 123456;
    int res = 0;
    for (int i = 0; i < int(prices.size()); i++) {
      premin = min(prices[i], premin);
      res = max(prices[i] - premin, res);
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
  vector<int> prices = {7, 1, 5, 3, 6, 4};
  cout << sl.maxProfit(prices) << endl;
#endif
  return 0;
}
