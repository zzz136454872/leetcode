from collections import deque
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        queue = deque()

        for num in arr:
            if len(queue) < k:
                queue.append(num)
            elif abs(queue[0] - x) > abs(num - x):
                queue.popleft()
                queue.append(num)

        return list(queue)


arr = [1, 2, 3, 4, 5]
k = 4
x = 3
arr = [1, 2, 3, 4, 5]
k = 4
x = -1
print(Solution().findClosestElements(arr, k, x))
