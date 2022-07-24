from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int,
                                destination: int) -> int:
        total = sum(distance)
        i = start
        tmp = 0

        while i != destination:
            tmp += distance[i]
            i = (i + 1) % len(distance)

        return min(tmp, total - tmp)


distance = [1, 2, 3, 4]
start = 0
destination = 1
distance = [1, 2, 3, 4]
start = 0
destination = 2
distance = [1, 2, 3, 4]
start = 0
destination = 3
print(Solution().distanceBetweenBusStops(distance, start, destination))
