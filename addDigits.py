from typing import List


class Solution:
    def addDigits(self, num: int) -> int:
        def wash(a):
            tmp = 0

            while a > 0:
                tmp += a % 10
                a = a // 10

            return tmp

        while num >= 10:
            num = wash(num)

        return num


num = 38
num = 0
print(Solution().addDigits(num))
