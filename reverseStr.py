class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)

        for i in range(n // (2 * k)):
            l = i * 2 * k
            r = l + k - 1

            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        l = n - n % (2 * k)
        r = min(l + k - 1, n - 1)

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return ''.join(s)


sl = Solution()
s = "abcdefg"
k = 2
print(sl.reverseStr(s, k))
