from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        cc = Counter(c.values())

        if len(cc) > 2:
            return False

        if len(cc) == 1:
            return max(cc.keys()) == 1 or cc[max(cc.keys())] == 1

        if max(cc.keys()) - min(cc.keys()) > 1:
            return min(cc.keys()) == 1 and cc[1] == 1

        return min(cc.keys()) == 1 and cc[1] == 1 or cc[max(
            cc.keys())] == 1 and max(cc.keys()) - min(cc.keys()) == 1


word = "abcc"
word = "aazz"
word = 'abbcc'
word = 'ddaccb'
word = 'cbccca'
word = 'zz'
print(Solution().equalFrequency(word))
