class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # primes=[2,3
        mod = 10**9 + 7

        def c(a, b):
            b = min(a - b, b)
            r = 1

            for i in range(b):
                r = r * (a - i) // (i + 1)

            return r

        def f(m):
            p = 2
            mem = {}

            while m != 1:
                while m % p == 0:
                    m //= p

                    if p in mem:
                        mem[p] += 1
                    else:
                        mem[p] = 1
                p += 1
            r = 1

            for v in mem.values():
                r = (r * c(v + n - 1, n - 1)) % mod

            return r

        return sum(f(i) for i in range(1, maxValue + 1)) % mod


n = 2
maxValue = 5
n = 5
maxValue = 3

print(Solution().idealArrays(n, maxValue))
