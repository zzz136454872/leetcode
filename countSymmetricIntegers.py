class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def su(a):
            return sum(int(l) for l in a)

        def isa(a):
            s = str(a)
            c = len(s)

            if c % 2 != 0:
                return False
            c //= 2

            return su(s[:c]) == su(s[c:])

        return [isa(i) for i in range(low, high + 1)].count(True)
