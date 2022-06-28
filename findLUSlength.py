from typing import List


# 不知道是哪个
class Solution0:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a), len(b))

        if a == b:
            return -1

        return len(a)


# a = "aba"
# b = "cdc"
# print(Solution().findLUSlength(a, b))


#  最长特殊序列 II
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSub(a, b):
            if len(a) < len(b):
                return False
            i = 0

            for j in range(len(b)):
                while i < len(a) and a[i] != b[j]:
                    i += 1

                if i == len(a):
                    return False
                i += 1

            return True

        strs.sort(key=lambda x: len(x), reverse=True)

        for i in range(len(strs)):
            flag = True

            for j in range(len(strs)):
                if i == j:
                    continue
                # print(i,j)

                if isSub(strs[j], strs[i]):
                    flag = False

                    break

            if flag:
                return len(strs[i])

        return -1


strs = ["aba", "cdc", "eae"]
strs = ["aaa", "aaa", "aa"]
strs = ["aabbcc", "aabbcc", "c", "e", "aabbcd"]
print(Solution().findLUSlength(strs))
