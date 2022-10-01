from typing import *


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '')
        number = number.replace('-', '')
        out = []

        while len(number) > 4:
            out.append(number[:3])
            number = number[3:]

        if len(number) == 4:
            out.append(number[:2])
            out.append(number[2:])
        else:
            out.append(number)

        return '-'.join(out)


sl = Solution()
number = "123 4-567"
print(sl.reformatNumber(number))
