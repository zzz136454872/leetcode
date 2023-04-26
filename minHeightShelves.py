from functools import cache
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def find(loc):
            if loc >= len(books):
                return 0
            m = 0
            width = 0
            res = 1234567

            for i in range(loc, len(books)):
                m = max(m, books[i][1])
                width += books[i][0]

                if width > shelfWidth:
                    break
                res = min(res, m + find(i + 1))

            return res

        return find(0)


books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
shelfWidth = 4
books = [[1, 3], [2, 4], [3, 2]]
shelfWidth = 6
print(Solution().minHeightShelves(books, shelfWidth))
