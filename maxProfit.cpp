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
// 不知道是哪个
class Solution1 {
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

// 买卖股票的最佳时机含冷静期
class Solution2 {
public:
  int maxProfit(vector<int> &prices) {
    int hold = -1234;
    int cold = 0;
    int sell = 0;
    int presell = 0;
    for (int &p : prices) {
      presell = sell;
      sell = max(sell, cold);
      cold = hold + p;
      hold = max(hold, presell - p);
      // cout<<p<<" "<<sell<<" "<<hold<<" "<<cold<<endl;
    }
    return max(sell, cold);
  }
};

// 714. 买卖股票的最佳时机含手续费
class Solution {
public:
  int maxProfit(vector<int> &prices, int fee) {
    int h = -prices[0];
    int u = 0;
    for (int i = 1; i < int(prices.size()); i++) {
      int nh = max(h, u - prices[i]);
      int nu = max(u, h + prices[i] - fee);
      h = nh;
      u = nu;
    }
    return u;
  }
};

#endif

int main() {
#ifdef testMod
  test();
#endif

#ifndef testMod
  // vector<int> prices = {7, 1, 5, 3, 6, 4};
  // cout << Solution().maxProfit(prices) << endl;
  // vector<int> prices = {1, 2, 3, 0, 2};
  // cout << Solution().maxProfit(prices) << endl;
  vector<int> prices = {1, 3, 2, 8, 4, 9};
  int fee = 2;
  cout << Solution().maxProfit(prices, fee) << endl;
#endif
  return 0;
}
