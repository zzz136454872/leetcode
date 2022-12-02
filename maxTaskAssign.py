from collections import deque
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int,
                      strength: int) -> int:
        workers.sort()
        tasks.sort()
        m = len(workers)

        def able(a):
            if a >= m:
                return False
            p = pills
            i = 0
            q = deque()

            for j in range(m - a - 1, m):
                while i <= a and workers[j] >= tasks[i] - strength:
                    q.append(tasks[i])
                    i += 1

                if len(q) == 0:
                    return False

                if workers[j] >= q[0]:
                    q.popleft()

                    continue

                if p <= 0:
                    return False
                p -= 1
                q.pop()

            return True

        l = 0
        r = len(tasks) - 1

        while l <= r:
            mid = (l + r) // 2
            print('left', l, 'right', r)

            if able(mid):
                l = mid + 1
            else:
                r = mid - 1

        return l


tasks = [3, 2, 1]
workers = [0, 3, 3]
pills = 1
strength = 1

tasks = [5, 4]
workers = [0, 0, 0]
pills = 1
strength = 5

tasks = [10, 15, 30]
workers = [0, 10, 10, 10, 10]
pills = 3
strength = 10

tasks = [74, 41, 64, 20, 28, 52, 30, 4, 4, 63]
workers = [38]
pills = 0
strength = 68
print(Solution().maxTaskAssign(tasks, workers, pills, strength))
