from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        mem = {}
        parent = {}
        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
            67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
            139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
            211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
            281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
            367, 373, 379, 383, 389, 397
        ]

        def find(a):
            if a not in parent:
                return a

            return find(parent[a])

        def union(a, b):
            a = find(a)
            b = find(b)

            if a != b:
                parent[max(a, b)] = min(a, b)

        for num in nums:
            mindiv = -1

            for prime in primes:
                if num % prime == 0:
                    if mindiv == -1:
                        mindiv = prime
                        mem[prime] = mem.get(prime, 0) + 1
                    else:
                        union(mindiv, prime)

                    while num % prime == 0:
                        num //= prime

                if prime * prime > num:
                    break

            if num > 1:
                if mindiv == -1:
                    mem[num] = mem.get(num, 0) + 1
                else:
                    union(mindiv, num)

        mem2 = {}

        for prime in mem:
            key = find(prime)
            mem2[key] = mem2.get(key, 0) + mem[prime]

        return max(max(mem2.values()), 1)


nums = [4, 6, 15, 35]
nums = [20, 50, 9, 63]
nums = [2, 3, 6, 7, 4, 12, 21, 39]
print(Solution().largestComponentSize(nums))
