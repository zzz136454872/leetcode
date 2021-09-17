from typing import List


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        mem = {'a': a, 'b': b, 'c': c}
        log = ['a', 'b', 'c']
        log.sort(key=lambda x: mem[x])

        while mem[log[0]] == 0:
            del log[0]

        out = ''

        while len(log) > 1:
            if len(out) == 0 or out[-1] != log[-1]:
                c = min(2, mem[log[-1]])
                mem[log[-1]] -= c
                out += log[-1] * c

                if mem[log[-1]] == 0:
                    log.pop()
            else:
                mem[log[-2]] -= 1
                out += log[-2]

                if mem[log[-2]] == 0:
                    log.pop(-2)
            log.sort(key=lambda x: mem[x])

        if len(out) == 0 or out[-1] != log[-1]:
            c = min(2, mem[log[-1]])
            mem[log[-1]] -= c
            out += log[-1] * c

        return out


a = 1
b = 1
c = 7
a = 2
b = 2
c = 1
a = 7
b = 1
c = 0

print(Solution().longestDiverseString(a, b, c))
