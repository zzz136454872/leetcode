from typing import *


class Solution:
    def intToRoman(self, num: int) -> str:
        chars = [
            'I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM',
            'M'
        ]
        ints = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        out = []

        for i in range(len(chars) - 1, -1, -1):
            while num >= ints[i]:
                out.append(chars[i])
                num = num - ints[i]

        return ''.join(out)


sl = Solution()
num = 1994
print(sl.intToRoman(num))
