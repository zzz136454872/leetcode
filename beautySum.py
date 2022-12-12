from collections import defaultdict


class Solution:
    def beautySum(self, s: str) -> int:
        tmp = defaultdict(int)
        mem = [tmp.copy()]

        for l in s:
            tmp[l] += 1
            mem.append(tmp.copy())

        def sub(a, b):
            m1 = 123456
            m2 = 0

            for k in b:
                d = b[k] - a[k]

                if d < m1 and d > 0:
                    m1 = d

                if d > m2:
                    m2 = d

            if m1 == 123456:
                return 0

            return m2 - m1

        res = 0

        for i in range(len(s) - 2):
            for j in range(i + 3, len(s) + 1):
                res += sub(mem[i], mem[j])

        return res


s = "aabcb"
s = "aabcbaa"
print(Solution().beautySum(s))
