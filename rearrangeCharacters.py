from collections import Counter, defaultdict


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        mem1 = Counter(target)
        mem2 = defaultdict(int, Counter(s))
        res = 123456

        for k, v in mem1.items():
            res = min(res, mem2[k] // v)

        return res


s = "ilovecodingonleetcode"
target = "code"
s = "abcba"
target = "abc"
s = "abbaccaddaeea"
target = "aaaaa"
print(Solution().rearrangeCharacters(s, target))
