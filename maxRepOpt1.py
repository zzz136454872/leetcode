from collections import defaultdict
from typing import List


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        mem = defaultdict(int)
        mem2 = defaultdict(int)
        mem3 = defaultdict(int)
        prev2 = 'kk'
        prev2Len = 0
        prev1 = 'aa'
        prev1Len = 0
        now = 'ff'
        nowLen = 0

        for l in text:
            mem[l] += 1

            if l == now:
                nowLen += 1
            else:
                prev2 = prev1
                prev2Len = prev1Len
                prev1 = now
                prev1Len = nowLen
                nowLen = 1
                now = l
            mem3[l] = max(mem3[l], nowLen)

            if prev1Len == 1 and now == prev2:
                mem2[l] = max(mem2[l], prev2Len + nowLen)

        # print('mem1',dict(mem))
        # print('mem2',dict(mem2))
        # print('mem3',dict(mem3))

        res = 0

        for k in mem.keys():
            tmp = mem3[k]

            if tmp < mem[k]:
                tmp += 1
            res = max(res, tmp)
            tmp = mem2[k]

            if tmp < mem[k]:
                tmp += 1
            res = max(res, tmp)

        return res


text = "ababa"
text = "aaabaaa"
text = "aaabbaaa"
text = "aaaaa"
text = "abcdef"
print(Solution().maxRepOpt1(text))
