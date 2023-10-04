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
  vector<int> findSquare(vector<vector<int>> &matrix) {
    mat = matrix;
    vector<int> res;
    cache = vector<vector<vector<int>>>(mat.size(),
                                        vector<vector<int>>(mat[0].size()));
    m = mat.size();
    n = mat[0].size();

    print(find(1, 0));

    for (int i = 0; i < int(mat.size()); i++) {
      for (int j = 0; j < int(mat[0].size()); j++) {
        if (mat[i][j] == 0) {
          auto tmp = find(i, j);
          int r = max(tmp[0], tmp[1]);
          if (res.size() == 0 || r > res[3]) {
            res = vector<int>{i, j, r};
          }
        }
      }
    }
    return res;
  }

private:
  vector<vector<int>> mat;
  vector<vector<vector<int>>> cache;
  int m, n;
  vector<int> find(int x, int y) {
    if (x < 0 || y < 0 || x >= m || y >= n || mat[x][y] == 1) {
      return vector<int>(2, 0);
    }

    if (cache[x][y].size() != 0) {
      return cache[x][y];
    }
    vector<int> l = find(x, y + 1);
    vector<int> d = find(x + 1, y);
    vector<int> res = {min(d[0] + 1, l[0]), min(d[1], l[1] + 1)};
    cache[x][y] = res;
    return res;
  }
};
#endif

int main() {
#ifdef testMod
  test();
#endif

#ifndef testMod
  Solution sl;
  vector<vector<int>> mat = {{1, 0, 1}, {0, 0, 1}, {0, 0, 1}};
  print(sl.findSquare(mat));
#endif
  return 0;
}
