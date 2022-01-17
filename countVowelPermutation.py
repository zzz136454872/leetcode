class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mem = [1 for i in range(5)]
        mod = 10**9 + 7

        for j in range(n - 1):
            nmem = []
            nmem.append(mem[1])
            nmem.append((mem[0] + mem[2]) % mod)
            nmem.append((mem[0] + mem[1] + mem[3] + mem[4]) % mod)
            nmem.append((mem[2] + mem[4]) % mod)
            nmem.append(mem[0])
            mem = nmem

        return sum(mem) % mod


n = 1
n = 5
print(Solution().countVowelPermutation(n))
