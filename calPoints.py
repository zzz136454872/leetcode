from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for op in ops:
            if op.isdigit() or op[1:].isdigit():
                stack.append(int(op))
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()

        return sum(stack)


ops = ["5", "2", "C", "D", "+"]
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
# ops = ["1"]
print(Solution().calPoints(ops))
