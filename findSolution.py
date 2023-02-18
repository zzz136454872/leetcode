from typing import List

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction',
                     z: int) -> List[List[int]]:
        f = customfunction.f
        res = []
        r = 1001

        for i in range(1, 1001):
            l = 1

            while l <= r:
                mid = (l + r) // 2
                v = f(i, mid)

                if v > z:
                    r = mid - 1
                elif v < z:
                    l = mid + 1
                else:
                    res.append([i, mid])
                    r = mid

                    break

        return res


class CustomFunction:
    def f(self, x, y):
        return x + y


z = 5
print(Solution().findSolution(CustomFunction(), z))
