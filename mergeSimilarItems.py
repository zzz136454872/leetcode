from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]],
                          items2: List[List[int]]) -> List[List[int]]:
        value = {}

        for v, w in items1:
            value[v] = value.get(v, 0) + w

        for v, w in items2:
            value[v] = value.get(v, 0) + w

        return sorted(list(value.items()))


items1 = [[1, 1], [4, 5], [3, 8]]
items2 = [[3, 1], [1, 5]]
items1 = [[1, 1], [3, 2], [2, 3]]
items2 = [[2, 1], [3, 2], [1, 3]]
items1 = [[1, 3], [2, 2]]
items2 = [[7, 1], [2, 2], [1, 4]]
print(Solution().mergeSimilarItems(items1, items2))
