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
  vector<string> letterCasePermutation(string s) {
    vector<string> tmp1 = {""};
    vector<string> tmp2;

    for (auto letter : s) {
      if (isdigit(letter)) {
        for (auto &ss : tmp1) {
          ss += letter;
        }
        continue;
      }
      if (isupper(letter)) {
        for (auto ss : tmp1) {
          tmp2.push_back(ss + char(tolower(letter)));
          tmp2.push_back(ss + letter);
        }
      } else {
        for (auto ss : tmp1) {
          tmp2.push_back(ss + letter);
          tmp2.push_back(ss + char(toupper(letter)));
        }
      }
      tmp1 = tmp2;
      tmp2 = vector<string>{};
    }
    return tmp1;
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

  string s = "a1b2";
  print(sl.letterCasePermutation(s));
#endif
  return 0;
}
