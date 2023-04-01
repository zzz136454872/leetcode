# 不知道是哪个
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def c1(loc):
            i = loc
            j = loc

            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            return (j - i) // 2

        def c2(loc):
            i = loc
            j = loc + 1

            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            return (j - i - 1) // 2

        out = 0

        for i in range(len(s)):
            out += c1(i) + c2(i)

        return out


# 1638. 统计只差一个字符的子串数目
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        res = 0

        for i in range(len(s)):
            for j in range(len(t)):
                d = 0

                for k in range(min(len(s) - i, len(t) - j)):
                    if s[i + k] != t[j + k]:
                        d += 1

                        if d > 1:
                            break

                    if d == 1:
                        res += 1

        return res


s = "aba"
t = "baba"
s = "ab"
t = "bb"
s = "a"
t = "a"
s = "abe"
t = "bbc"
print(Solution().countSubstrings(s, t))
