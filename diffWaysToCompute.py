from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        lis = []
        k = 0

        for letter in expression:
            if letter.isdigit():
                k = k * 10 + int(letter)
            else:
                lis.append(k)
                lis.append(letter)
                k = 0
        lis.append(k)

        def op(a, operator, b):
            if operator == '+':
                return a + b

            if operator == '-':
                return a - b

            return a * b

        def compute(l, r):
            if l == r:
                return [lis[l]]

            res = []

            for i in range(l + 1, r, 2):
                r1 = compute(l, i - 1)
                r2 = compute(i + 1, r)

                for num1 in r1:
                    for num2 in r2:
                        res.append(op(num1, lis[i], num2))

            return res

        return compute(0, len(lis) - 1)


expression = "2*3-4*5"
expression = "2-1-1"
print(Solution().diffWaysToCompute(expression))
