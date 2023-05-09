class Solution:
    def countTime(self, time: str) -> int:
        t1, t2 = time.split(':')
        k1 = 1
        k2 = 1

        if '?' in t1:
            if t1 == '??':
                k1 = 24
            elif t1[0] == '?':
                if ord(t1[1]) < ord('4'):
                    k1 = 3
                else:
                    k1 = 2
            else:
                if t1[0] == '2':
                    k1 = 4
                else:
                    k1 = 10

        if '?' in t2:
            if t2 == '??':
                k2 = 60
            elif t2[0] == '?':
                k2 = 6
            else:
                k2 = 10

        return k1 * k2


time = "?5:00"
time = "0?:0?"
time = "??:??"
time = '?2:16'
time = '07:?3'

print(Solution().countTime(time))
