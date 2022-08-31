from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        i = 0
        stack = []

        for num in popped:

            if len(stack) > 0 and stack[-1] == num:
                stack.pop()

                continue

            while i < len(pushed) and pushed[i] != num:
                stack.append(pushed[i])
                i += 1

            if i == len(pushed):
                return False
            i += 1

        return i == len(pushed)


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
print(Solution().validateStackSequences(pushed, popped))
