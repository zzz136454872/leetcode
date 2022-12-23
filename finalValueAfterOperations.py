from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        mem = {'++X': 1, 'X++': 1, '--X': -1, 'X--': -1}

        return sum(mem[x] for x in operations)


operations = ["--X", "X++", "X++"]
operations = ["++X", "++X", "X++"]
operations = ["X++", "++X", "--X", "X--"]
print(Solution().finalValueAfterOperations(operations))
