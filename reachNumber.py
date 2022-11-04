class Solution:
    def reachNumber(self, target: int) -> int:
        k = 0
        s = 0
        target = abs(target)

        while s < target:
            k += 1
            s += k
        d = s - target

        if d % 2 == 0:
            return k
        k += 1

        if (k - d) % 2 != 0:
            k += 1

        return k


target = 2
print(Solution().reachNumber(target))
