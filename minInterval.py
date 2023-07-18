from heapq import heappop, heappush
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]],
                    queries: List[int]) -> List[int]:
        queries = sorted([[queries[i], i] for i in range(len(queries))])
        intervals.sort()
        i = 0
        heap = []

        for q in queries:
            while i < len(intervals) and intervals[i][0] <= q[0]:
                heappush(heap,
                         (intervals[i][1] - intervals[i][0], intervals[i][1]))
                i += 1

            while len(heap) > 0 and heap[0][1] < q[0]:
                heappop(heap)

            if len(heap) > 0:
                q.append(heap[0][0] + 1)
            else:
                q.append(-1)
        queries.sort(key=lambda x: x[1])

        return [q[2] for q in queries]


intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
print(Solution().minInterval(intervals, queries))
