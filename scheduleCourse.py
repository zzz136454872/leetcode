from heapq import heappop, heappush
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap = []
        total = 0

        for c in courses:
            if total + c[0] <= c[1]:
                total += c[0]
                heappush(heap, (-c[0], c[1]))
            elif len(heap) > 0 and -heap[0][0] > c[0]:
                total += heap[0][0]
                total += c[0]
                heappop(heap)
                heappush(heap, (-c[0], c[1]))

        return len(heap)


courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
courses = [[1, 2]]
courses = [[3, 2], [4, 3]]
print(Solution().scheduleCourse(courses))
