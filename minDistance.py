class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        mem = [[-1] * n for i in range(m)]

        def lcs(loc1, loc2):
            if loc1 == m or loc2 == n:
                return 0

            if mem[loc1][loc2] != -1:
                return mem[loc1][loc2]

            if word1[loc1] == word2[loc2]:
                out = 1 + lcs(loc1 + 1, loc2 + 1)
            else:
                out = max(lcs(loc1 + 1, loc2), lcs(loc1, loc2 + 1))
            mem[loc1][loc2] = out

            return out

        return n + m - 2 * lcs(0, 0)


s1 = "sea"
s2 = "eat"
print(Solution().minDistance(s1, s2))
