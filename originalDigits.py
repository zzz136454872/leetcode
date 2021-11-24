from typing import *

# zero one two three four five six seven eight nine
# z=0
#


class Solution:
    def originalDigits(self, s: str) -> str:
        alphabet = 'abcdefghigklmnopqrstuvwxyz'
        log = {}

        for letter in alphabet:
            log[letter] = 0

        for letter in s:
            log[letter] += 1
        count = [0 for i in range(10)]
        count[0] = log['z']
        count[2] = log['w']
        count[4] = log['u']
        count[6] = log['x']
        count[8] = log['g']
        count[3] = log['h'] - log['g']
        count[7] = log['s'] - count[6]
        count[5] = log['v'] - count[7]
        count[9] = log['i'] - count[5] - count[6] - count[8]
        count[1] = log['n'] - count[7] - 2 * count[9]
        out = ''

        for i in range(10):
            out += count[i] * str(i)

        return out


sl = Solution()
s = 'fviefuro'
print(sl.originalDigits(s))
