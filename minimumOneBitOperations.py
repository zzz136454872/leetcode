class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        mem1 = {}
        mem2 = {}

        def take0(loc):
            if loc < 0:
                return 0
            nonlocal n

            if n & (1 << loc) == 0:
                return 0

            if (loc, n & (2**(loc + 1) - 1)) in mem1:
                tmp = mem1[(loc, n & (2**(loc + 1) - 1))]
                n = n & ((2**31 - 1) ^ (2**(loc + 1) - 1)) | tmp[1]

                return tmp[0]

            oriLow = n & (2**(loc + 1) - 1)
            res = 0
            res += take1(loc - 1)

            for i in range(loc - 2, -1, -1):
                res += take0(i)
            res += 1
            n &= (2**31 - 1) ^ (1 << loc)
            mem1[(loc, oriLow)] = (res, n & (2**(loc + 1) - 1))

            return res

        def take1(loc):
            if loc < 0:
                return 0
            nonlocal n

            if n & (1 << loc) != 0:
                return 0

            if (loc, n & (2**(loc + 1) - 1)) in mem2:
                tmp = mem2[(loc, n & (2**(loc + 1) - 1))]
                n = n & ((2**31 - 1) ^ (2**(loc + 1) - 1)) | tmp[1]

                return tmp[0]

            oriLow = n & (2**(loc + 1) - 1)
            res = 0
            res += take1(loc - 1)

            for i in range(loc - 2, -1, -1):
                res += take0(i)
            res += 1
            n |= 1 << loc
            mem2[(loc, oriLow)] = (res, n & (2**(loc + 1) - 1))

            return res

        loc = 0

        while 2**loc <= n:
            loc += 1
        loc -= 1
        res = 0

        while loc >= 0:
            if n & (1 << loc) != 0:
                res += take0(loc)
            loc -= 1

        return res


n = 3
n = 6
n = 6091090
print(Solution().minimumOneBitOperations(n))
