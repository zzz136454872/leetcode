from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def valid(s):
            # print('ss',s)

            if len(s) < 2:
                return True

            if s[0] == '0' and s[1] != '.':
                return False

            if '.' not in s:
                return True
            loc = s.index('.')
            p1 = s[:loc]
            p2 = s[loc + 1:]

            if len(p2) == 0 or p2[-1] == '0':
                return False

            return True

        def cut(a):
            out = []

            for j in range(1, len(a)):
                tmp = a[:j] + '.' + a[j:]

                if valid(tmp):
                    out.append(tmp)

            if valid(a):
                out.append(a)

            return out

        s = s[1:len(s) - 1]
        res = []
        # print('s',s)

        for i in range(1, len(s)):
            l = cut(s[:i])
            r = cut(s[i:])
            # print(i,l,r)

            for a in l:
                for b in r:
                    res.append('(' + a + ', ' + b + ')')

        return res


s = "(123)"
s = "(00011)"
s = "(0123)"
s = "(100)"
print(Solution().ambiguousCoordinates(s))
