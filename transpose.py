from typing import *

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(i) for i in zip(*matrix)]
