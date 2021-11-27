from typing import *


class Solution:
    def __init__(self, n_rows: int, n_cols: int):
        self.rows = n_rows
        self.cols = n_cols
        self.log = set()
        self.size = n_rows * n_cols
        self.now = 1

    def rand(self):
        self.now = (self.now * 359981) % 100000007

        return self.now % self.size

    def toNum(self, point):
        pass

    def toPoint(self, num):
        return [num // self.cols, num % self.cols]

    def flip(self) -> List[int]:
        num = self.rand()

        while num in self.log:
            num = (num + 1) % self.size
        self.log.add(num)

        return self.toPoint(num)

    def reset(self) -> None:
        self.log = set()


sl = Solution(1, 2)

for i in range(2):
    print(sl.flip())
