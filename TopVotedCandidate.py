from typing import List


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        mem = [0] * len(persons)
        self.log = []
        maxValue = 0
        maxLoc = -1

        for i in range(len(persons)):
            p = persons[i]
            now = times[i]
            mem[p] += 1

            if mem[p] >= maxValue:
                if p != maxLoc:
                    self.log.append((now, p))
                    maxLoc = p
                maxValue = mem[p]

    def q(self, t: int) -> int:
        l = 0
        r = len(self.log) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.log[mid][0] <= t:
                l = mid + 1
            else:
                r = mid - 1

        return self.log[r][1]
