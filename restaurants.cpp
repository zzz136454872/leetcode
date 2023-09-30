/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
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
  vector<int> filterRestaurants(vector<vector<int>> &restaurants,
                                int veganFriendly, int maxPrice,
                                int maxDistance) {

    vector<vector<int>> res;
    for (int i = 0; i < int(restaurants.size()); i++) {
      auto r = restaurants[i];
      if (r[2] == 0 and veganFriendly == 1)
        continue;
      if (r[3] > maxPrice)
        continue;
      if (r[4] > maxDistance) {
        continue;
      }
      res.push_back(r);
    }
    sort(res.begin(), res.end(), [](vector<int> &a, vector<int> &b) {
      if (a[1] != b[1]) {
        return a[1] > b[1];
      } else {
        return a[0] > b[0];
      }
    });
    vector<int> res2;
    for (auto r : res) {
      res2.push_back(r[0]);
    }
    return res2;
  }

private:
};
#endif

int main() {
#ifdef testMod
  test();
#endif

#ifndef testMod
  vector<vector<int>> restaurants = {{1, 4, 1, 40, 10},
                                     {2, 8, 0, 50, 5},
                                     {3, 8, 1, 30, 4},
                                     {4, 10, 0, 10, 3},
                                     {5, 1, 1, 15, 1}};
  int veganFriendly = 1, maxPrice = 50, maxDistance = 10;
  restaurants = {{1, 4, 1, 40, 10},
                 {2, 8, 0, 50, 5},
                 {3, 8, 1, 30, 4},
                 {4, 10, 0, 10, 3},
                 {5, 1, 1, 15, 1}};
  veganFriendly = 0, maxPrice = 50, maxDistance = 10;
  restaurants = {{1, 4, 1, 40, 10},
                 {2, 8, 0, 50, 5},
                 {3, 8, 1, 30, 4},
                 {4, 10, 0, 10, 3},
                 {5, 1, 1, 15, 1}};
  veganFriendly = 0, maxPrice = 30, maxDistance = 3;
  print(Solution().filterRestaurants(restaurants, veganFriendly, maxPrice,
                                     maxDistance));
#endif
  return 0;
}
