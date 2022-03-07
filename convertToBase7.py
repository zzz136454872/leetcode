from typing import List


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        out = ''
        flag = False

        if num < 0:
            flag = True
            num = -num

        while num > 0:
            out = str(num % 7) + out
            num = num // 7

        if flag:
            out = '-' + out

        return out


num = 100
# num = -7
print(Solution().convertToBase7(num))
