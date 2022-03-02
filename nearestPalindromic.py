class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def isPali(n):
            return n == n[::-1]

        sn = n
        l = len(sn)
        mem = []

        if l % 2 == 0:
            lp1 = sn[:l // 2]
            t1 = lp1 + lp1[::-1]
            mem.append(t1)
            lp1 = str(int(sn[:l // 2]) + 1)
            t1 = lp1 + lp1[::-1]
            mem.append(t1)
            lp1 = str(int(sn[:l // 2]) - 1)
            t1 = lp1 + lp1[::-1]
            mem.append(t1)
        else:
            lp1 = sn[:l // 2 + 1]
            t1 = lp1 + lp1[-2::-1]
            mem.append(t1)
            lp2 = str(int(sn[:l // 2 + 1]) + 1)
            t1 = lp2 + lp2[-2::-1]
            mem.append(t1)

            if lp1 != '0':
                lp1 = str(int(sn[:l // 2 + 1]) - 1)
                # print(lp1)
                t1 = lp1 + lp1[-2::-1]
                mem.append(t1)
        # print(mem)

        if l > 1:
            mem.append('9' * (l - 1))
        mem.append('1' + '0' * (l - 1) + '1')
        mem.sort(key=lambda x: (abs(int(x) - int(n))
                                if x != n else 123456789987654312, int(x)))

        return mem[0]


sl = Solution()
inp = [0, 1, 10, 11, 100]

for n in inp:
    print(n, sl.nearestPalindromic(str(n)))
