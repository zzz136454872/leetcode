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
  vector<int> fullBloomFlowers(vector<vector<int>> &flowers,
                               vector<int> &people) {
    map<int, int> mem = {};
    for (auto f : flowers) {
      if (mem.count(f[0]) == 1) {
        mem[f[0]]++;
      } else {
        mem[f[0]] = 1;
      }
      int k2 = f[1] + 1;
      if (mem.count(k2) == 1) {
        mem[k2]--;
      } else {
        mem[k2] = -1;
      }
    }

    vector<vector<int>> mem2 = {};

    for (auto it = mem.begin(); it != mem.end(); it++) {
      if (it->second == 0)
        continue;
      mem2.push_back(vector<int>{it->first, it->second});
    }
    sort(mem2.begin(), mem2.end(),
         [](vector<int> &a, vector<int> &b) { return a[0] < b[0]; });
    vector<vector<int>> ps;

    for (int i = 0; i < int(people.size()); i++) {
      ps.push_back(vector<int>{people[i], i, 0});
    }

    sort(ps.begin(), ps.end(),
         [](vector<int> &a, vector<int> &b) { return a[0] < b[0]; });

    int j = 0;
    int tmp = 0;

    for (int i = 0; i < int(ps.size()); i++) {
      while (j < int(mem2.size()) && mem2[j][0] <= ps[i][0]) {
        tmp += mem2[j][1];
        j++;
      }
      ps[i][2] = tmp;
    }
    sort(ps.begin(), ps.end(),
         [](vector<int> &a, vector<int> &b) { return a[1] < b[1]; });
    vector<int> res;
    for (auto p : ps) {
      res.push_back(p[2]);
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
  vector<vector<int>> flowers = {{1, 6}, {3, 7}, {9, 12}, {4, 13}};
  vector<int> people = {2, 3, 7, 11};
  flowers = {{1, 10}, {3, 3}};
  people = {3, 3, 2};
  print(sl.fullBloomFlowers(flowers, people));
#endif
  return 0;
}
