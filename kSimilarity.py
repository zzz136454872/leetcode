class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        mem = {"": 0}

        def sub(s):
            if s in mem:
                return mem[s]
            j = len(s1) - len(s)

            if s[0] == s1[j]:
                res = sub(s[1:])
            else:
                res = len(s)

                for i in range(1, len(s)):
                    if s[i] == s1[j]:
                        # print('flag',i,j,s,s1[j:],s[1:i]+s[0]+s[i+1:])
                        res = min(sub(s[1:i] + s[0] + s[i + 1:]) + 1, res)
            mem[s] = res
            # print(s,s1[j:],res)

            return res

        return sub(s2)


s1 = "ab"
s2 = "ba"
# s1 = "abc"
# s2 = "bca"
s1 = "bccaba"
s2 = "abacbc"
print(Solution().kSimilarity(s1, s2))
