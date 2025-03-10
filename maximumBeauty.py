from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]],
                      queries: List[int]) -> List[int]:
        res = 0
        items.sort()
        mem = []
        qs = [[i, queries[i]] for i in range(len(queries))]
        qs.sort(key=lambda x: x[-1])
        j = 0

        for i in range(len(qs)):
            while j < len(items) and items[j][0] <= qs[i][1]:
                res = max(res, items[j][1])
                j += 1
            qs[i].append(res)
        qs.sort()

        return [q[2] for q in qs]


items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
queries = [1, 2, 3, 4, 5, 6]
items = [[1, 2], [1, 2], [1, 3], [1, 4]]
queries = [1]
items = [[10, 1000]]
queries = [5]
print(Solution().maximumBeauty(items, queries))
