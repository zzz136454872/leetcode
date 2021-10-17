class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'

        for i in range(n - 1):
            s = self.say(s)

        return s

    def say(self, s):
        out = ''

        while len(s) > 0:
            p = s[0]
            i = 1

            while (s[:i].count(p) == i):
                i += 1
            i -= 1
            out += str(i) + p
            s = s[i:]

        return out


sl = Solution()
print(sl.countAndSay(3))
