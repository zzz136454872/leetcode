from collections import deque
from typing import List


# wa
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int,
                     x: int) -> int:
        if x == 0:
            return 0
        mem = {}

        for f in forbidden:
            mem[f] = -1
        queue = deque([[0, 0]])

        for i in range(10000):
            print(i, queue, mem)

            if len(queue) == 0:
                return -1
            now = queue.popleft()

            if now[0] > b and now[0] - b not in mem:
                if now[0] - b == x:
                    return now[1] + 1
                mem[now[0] - b] = now[1] + 1
                queue.append((now[0] - b, now[1] + 1))

            if now[0] + a not in mem:
                if now[0] + a == x:
                    return now[1] + 1
                mem[now[0] + a] = now[1] + 1
                queue.append((now[0] + a, now[1] + 1))

        return -1


forbidden = [14, 4, 18, 1, 15]
a = 3
b = 15
x = 9
forbidden = [8, 3, 16, 6, 12, 20]
a = 15
b = 13
x = 11
# forbidden = [1,6,2,14,5,17,4]
# a = 16
# b = 9
# x = 7
print(Solution().minimumJumps(forbidden, a, b, x))
