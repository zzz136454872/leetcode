from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        mem = {}
        mem[keysPressed[0]] = releaseTimes[0]

        for i in range(1, len(keysPressed)):
            mem[keysPressed[i]] = max(mem.get(keysPressed[i], 0),
                                      releaseTimes[i] - releaseTimes[i - 1])

        out = 'a'
        c = 0

        for k, v in mem.items():
            if v > c or v == c and ord(k) > ord(out):
                out = k
                c = v

        return out


releaseTimes = [9, 29, 49, 50]
keysPressed = "cbcd"
print(Solution().slowestKey(releaseTimes, keysPressed))
