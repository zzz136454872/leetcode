from collections import deque
from typing import List


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.total = 0
        self.length = 0
        self.mem = deque()

    def next(self, val: int) -> float:
        self.total += val
        self.mem.append(val)

        if self.length == self.size:
            self.total -= self.mem.popleft()
        else:
            self.length += 1

        return self.total / self.length


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
