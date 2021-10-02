from typing import List


class Solution:
    def toHex(self, num: int) -> str:
        singleHex = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
            'd', 'e', 'f'
        ]

        if num == 0:
            return '0'

        if num < 0:
            num = -num
            num = ((2**32 - 1) ^ num) + 1

        out = ''

        while num != 0:
            out = str(singleHex[num % 16]) + out
            num //= 16

        return out


num = 26
# num=-1
print(Solution().toHex(num))
