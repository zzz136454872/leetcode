class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    xy += 1
                else:
                    yx += 1

        if (xy + yx) % 2 != 0:
            return -1

        return xy // 2 + yx // 2 + 2 * (xy % 2)


s1 = "xx"
s2 = "yy"
s1 = "xy"
s2 = "yx"
s1 = "xx"
s2 = "xy"
s1 = "xxyyxyxyxx"
s2 = "xyyxyxxxyx"
print(Solution().minimumSwap(s1, s2))
