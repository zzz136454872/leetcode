class Solution:
    def minimumDeletions(self, s: str) -> int:
        mem1 = []
        t = 0

        for letter in s:
            if letter == 'b':
                t += 1
            mem1.append(t)
        c = 0
        mem2 = [0 for i in range(len(s) + 1)]

        for i in range(len(s) - 1, -1, -1):
            mem2[i] = mem2[i + 1]

            if s[i] == 'a':
                mem2[i] += 1
        res = len(s)

        for i in range(len(s)):
            res = min(res, mem1[i] + mem2[i])

        return res - 1


s = "aababbab"
s = "bbaaaaabb"
print(Solution().minimumDeletions(s))
