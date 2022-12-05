from collections import deque
from typing import List


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int,
                      maxBoxes: int, maxWeight: int) -> int:
        sig = [0]

        for i in range(1, len(boxes)):
            if boxes[i][0] == boxes[i - 1][0]:
                sig.append(sig[-1])
            else:
                sig.append(sig[-1] + 1)
        totalWeight = 0
        right = len(boxes)
        mem = [0] * (len(boxes) + 1)
        q = deque()

        for i in range(len(boxes) - 1, -1, -1):
            totalWeight += boxes[i][1]
            v = mem[i + 1] + sig[i]

            while len(q) > 0 and q[-1] > v:
                q.pop()
            q.append(v)

            while right - i > maxBoxes or totalWeight > maxWeight:
                right -= 1
                totalWeight -= boxes[right][1]

                if mem[right + 1] + sig[right] == q[0]:
                    q.popleft()
            mem[i] = q[0] + 2 - sig[i]

        return mem[0]


boxes = [[1, 1], [2, 1], [1, 1]]
portsCount = 2
maxBoxes = 3
maxWeight = 3

boxes = [[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]]
portsCount = 3
maxBoxes = 3
maxWeight = 6

boxes = [[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]]
portsCount = 3
maxBoxes = 6
maxWeight = 7

boxes = [[2, 4], [2, 5], [3, 1], [3, 2], [3, 7], [3, 1], [4, 4], [1, 3],
         [5, 2]]
# boxes = [[4,4],[1,3],[5,2]]
portsCount = 5
maxBoxes = 5
maxWeight = 7

boxes = [[1, 1], [2, 1], [1, 1], [2, 1], [1, 1], [2, 1]]
portsCount = 2
maxBoxes = 10
maxWeight = 10

print(Solution().boxDelivering(boxes, portsCount, maxBoxes, maxWeight))
