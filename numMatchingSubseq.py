from collections import deque
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        nxt = deque()
        tmp = [-1] * 26
        nxt.appendleft(tmp.copy())

        def l2n(a):
            return ord(a) - ord('a')

        for i in range(len(s) - 1, -1, -1):
            tmp[l2n(s[i])] = i
            nxt.appendleft(tmp.copy())
        nxt = list(nxt)

        res = 0

        for word in words:
            inside = True
            i = 0

            for letter in word:
                i = nxt[i][l2n(letter)]

                if i == -1:
                    inside = False

                    break
                i += 1

            if inside:
                res += 1

        return res


s = "abcde"
words = ["a", "bb", "acd", "ace"]
s = "dsahjpjauf"
words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
s = "iwdlcxpyagegrcnrcylxolxlnhhwnxyzltiscrjztiivnpnzlubzpueihinsqdfvypdteztiodbhaqhxskupwulvkzhczdyoouym"
words = [
    "hhwnxyzltiscrjztiivnpnzlubzpueihinsqdfvyp",
    "vnpnzlubzpueihinsqdfvypdteztiodbha",
    "rcnrcylxolxlnhhwnxyzltiscrjztiivnpnzlubzpueihi",
    "dfvypdteztiodbhaqhxskupwulvk", "zltiscrjztii",
    "wdmbatbcewwittubryrqwwrvfkrmniomofygybeqfzusrgeart",
    "myzfexqmzxnbmmnhmpbddqhrwrobqzjiwdzzpyzodejysuuquc",
    "wxvrcbihbasohfvuwuxleesqeujxvjfvgwnhltenbspdgzsdrs",
    "nztyysfhfbfcihyeaqdarqxfpjunevabzafvbmpbtenarvyizv",
    "nivufheyodfjuggrbndyojeahrzgptikjfqufhwyhzyyjteahx"
]
print(Solution().numMatchingSubseq(s, words))
