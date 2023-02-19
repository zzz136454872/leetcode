class Solution:
    def balancedString(self, s: str) -> int:
        mem = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        t = len(s) // 4

        for l in s:
            mem[l] += 1
        miss = set()

        for k in mem:
            if mem[k] > t:
                miss.add(k)

        for r in range(len(s)):
            if len(miss) == 0:
                break
            mem[s[r]] -= 1

            if mem[s[r]] == t:
                miss.discard(s[r])

        res = r

        for l in range(len(s)):
            mem[s[l]] += 1

            while mem[s[l]] > t and r < len(s):
                mem[s[r]] -= 1
                r += 1

            if mem[s[l]] > t:
                break

            if r <= l:
                r = l + 1
            res = min(res, r - l - 1)

        return res


s = "QWER"
s = "QQWE"
s = "QQQW"
s = "QQQQ"
s = "WQWRQQQW"
print(Solution().balancedString(s))
