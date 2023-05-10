class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        a = [1]
        seen = set(a)

        while True:
            a.append((a[-1] * 10 + 1) % k)

            if a[-1] == 0:
                return len(a)

            if a[-1] in seen:
                return -1
            seen.add(a[-1])


k = 1
k = 2
k = 3
print(Solution().smallestRepunitDivByK(k))
