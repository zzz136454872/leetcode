/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

//显示中间结果
void print(vector<int> a) {
  for (int i = 0; i < (int)a.size(); i++)
    cout << a[i] << " ";
  cout << endl;
}

void print(vector<vector<int>> a) {
  for (int i = 0; i < (int)a.size(); i++) {
    for (int j = 0; j < (int)a[i].size(); j++)
      cout << a[i][j] << " ";
    cout << endl;
  }
}

void print(vector<bool> a) {
  for (int i = 0; i < (int)a.size(); i++) {
    cout << i << " ";
    if (a[i])
      cout << "true ";
    else
      cout << "false ";
  }
  cout << endl;
}

void print(bool a[], int len) {
  for (int i = 0; i < len; i++) {
    cout << i << " ";
    if (a[i])
      cout << "true ";
    else
      cout << "false ";
  }
  cout << endl;
}

//#define testMod

#ifdef testMod
void test() {}
#endif

#ifndef testMod
class Solution {
public:
  vector<int> twoSum(vector<int> &numbers, int target) {
    int i = 0, j = numbers.size() - 1;
    vector<int> out;
    int tmp;
    while (i < j) {
      tmp = numbers[i] + numbers[j];
      if (tmp == target) {
        out.push_back(i + 1);
        out.push_back(j + 1);
        return out;
      } else if (tmp > target)
        j--;
      else
        i++;
    }
    return out;
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

#endif
  return 0;
}
