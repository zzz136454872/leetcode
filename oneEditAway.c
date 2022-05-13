#include "ctools.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#define testMod
#ifdef testMod
void test() {}
#endif

#define max(a, b) (((a) > (b)) ? (a) : (b))
#define min(a, b) (((a) < (b)) ? (a) : (b))

#ifndef testMod
// your code here
bool oneEditAway(char *first, char *second) {
  int l1 = strlen(first);
  int l2 = strlen(second);
  int i = 0;
  if (l1 == l2) {
    while (first[i] != 0 && first[i] == second[i])
      i++;
    if (i == l1)
      return true;
    return strcmp(first + i + 1, second + i + 1) == 0;
  } else if (l1 == l2 + 1) {
    while (first[i] != 0 && first[i] == second[i])
      i++;
    return strcmp(first + i + 1, second + i) == 0;
  } else if (l1 == l2 - 1) {
    while (first[i] != 0 && first[i] == second[i])
      i++;
    return strcmp(first + i, second + i + 1) == 0;
  } else {
    return false;
  }
  return false; // not here
}
#endif

int main() {
#ifdef testMod
  test();
#endif
#ifndef testMod
  char *first = "pale";
  char *second = "ple";
  first = "pales";
  second = "pal";
  printf("%d \n", oneEditAway(first, second));
#endif
  return 0;
}
