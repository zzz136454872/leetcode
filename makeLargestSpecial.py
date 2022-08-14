from functools import reduce


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        ctr = 0
        flag = False
        left = 0
        tmp = []

        for i in range(len(s)):

            if s[i] == '0':
                ctr -= 1

                if ctr == 0:
                    s1 = '1' + self.makeLargestSpecial(s[left + 1:i]) + '0'
                    tmp.append(s1)
                    left = i + 1
            else:
                ctr += 1

        tmp.sort(reverse=True)

        return reduce(lambda x, y: x + y, tmp)


s = "11011000"
print(Solution().makeLargestSpecial(s))
