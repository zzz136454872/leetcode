class Solution:
    def uniqueLetterString(self, s: str) -> int:
        s = [ord(a) - ord('A') for a in s]
        res = 0

        for i in range(26):
            prev = -1
            prev2 = -1

            for j in range(len(s)):
                if s[j] == i:
                    res += (prev - prev2) * (j - prev)
                    prev, prev2 = j, prev
            res += (prev - prev2) * (len(s) - prev)

        return res


s = "ABC"
s = "ABA"
s = "LEETCODE"
print(Solution().uniqueLetterString(s))
