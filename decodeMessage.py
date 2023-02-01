from typing import List


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mem = {}
        c = 0

        for l in key:
            if l not in mem and l.islower():
                mem[l] = chr(ord('a') + c)
                c += 1
        res = []

        for l in message:
            if l in mem:
                res.append(mem[l])
            else:
                res.append(l)

        return ''.join(res)


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

print(Solution().decodeMessage(key, message))
