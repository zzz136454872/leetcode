class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        remain = len(s) % k
        i = remain
        out = []

        if remain != 0:
            out.append(s[:remain])

        while i < len(s):
            out.append(s[i:i + k])
            i += k

        return '-'.join(out)


S = "5F3Z-2e-9-w"
K = 4
# S = "2-5g-3-J"
# K = 2
print(Solution().licenseKeyFormatting(S, K))
