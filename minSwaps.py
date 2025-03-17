# 不知道是哪个
class Solution1:
    def minSwaps(self, s: str) -> int:
        dic = {'0': 0, '1': 0}

        for letter in s:
            dic[letter] += 1

        s0 = dic['0']
        s1 = dic['1']

        if abs(s0 - s1) > 1:
            return -1

        def count(sp):
            e = 0

            for i in range(len(s)):
                if i % 2 == 0:
                    if s[i] != sp:
                        e += 1
                else:
                    if s[i] == sp:
                        e += 1

            return e // 2

        if s0 == s1:
            return min(count('0'), count('1'))

        if s0 > s1:
            return count('0')

        return count('1')


sl = Solution1()
s = "1000101011"

# print(sl.minSwaps(s))

# 1963. 使字符串平衡的最小交换次数


class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        c = 0

        for l in s:
            if l == ']':
                c += 1
                res = max(res, c)
            else:
                c -= 1

        return (res + 1) // 2


s = "][]["
s = "]]][[["
print(Solution().minSwaps(s))
