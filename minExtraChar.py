from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)

        res = [1234] * (len(s) + 1)
        res[-1] = 0

        for i in range(len(s) - 1, -1, -1):
            res[i] = len(s) - i

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in d:
                    res[i] = min(res[i], res[j])
                else:
                    res[i] = min(res[i], res[j] + j - i)

        return res[0]


s = "leetscode"
dictionary = ["leet", "code", "leetcode"]
s = "sayhelloworld"
dictionary = ["hello", "world"]
print(Solution().minExtraChar(s, dictionary))
