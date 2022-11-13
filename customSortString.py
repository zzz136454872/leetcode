from collections import defaultdict
from typing import List


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mem = defaultdict(lambda: 26)

        for i in range(len(order)):
            mem[order[i]] = i

        return ''.join(sorted(list(s), key=lambda x: mem[x]))


order = "cba"
s = "abcd"
order = "cbafg"
s = "abcd"
print(Solution().customSortString(order, s))
