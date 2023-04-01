from functools import cache


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(s1, s2):
            @cache
            def sub(i, j):
                if i == len(s1) or j == len(s2):
                    return ""

                if s1[i] == s2[j]:
                    return s1[i] + sub(i + 1, j + 1)
                t1 = sub(i + 1, j)
                t2 = sub(i, j + 1)

                if len(t1) > len(t2):
                    return t1

                return t2

            return sub(0, 0)

        c = lcs(str1, str2)

        def cut(s, t):
            res = []

            for letter in t:
                loc = s.find(letter)
                res.append(s[:loc])
                s = s[loc + 1:]
            res.append(s)

            return res

        str1 = cut(str1, c)
        str2 = cut(str2, c)
        res = []

        for i in range(len(c)):
            res.append(str1[i])
            res.append(str2[i])
            res.append(c[i])
        res.append(str1[-1])
        res.append(str2[-1])

        return ''.join(res)


str1 = "abac"
str2 = "cab"
print(Solution().shortestCommonSupersequence(str1, str2))
