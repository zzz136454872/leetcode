from typing import List


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        parent = [i for i in range(10**5 + 1)]

        # parent=[i for i in range(30)]

        def find(loc):
            while parent[loc] != loc:
                loc = parent[loc]

            return loc

        def merge(loc1, loc2):
            p1 = find(loc1)
            p2 = find(loc2)
            parent[max(p1, p2)] = min(p1, p2)

        prime = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
            67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
            139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
            211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
            281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
            367, 373, 379, 383, 389, 397, 401, 409
        ]

        for num in nums:
            tmp = num

            for i in range(len(prime)):
                if prime[i] * prime[i] > num:
                    break

                if tmp % prime[i] != 0:
                    continue

                while tmp % prime[i] == 0:
                    tmp //= prime[i]
                # print('merge',prime[i],num)
                merge(prime[i], num)

            if tmp > 1:
                merge(tmp, num)
        # print(parent)
        nums1 = nums.copy()
        nums.sort()

        for i in range(len(nums)):
            if find(nums[i]) != find(nums1[i]):
                return False

        return True


nums = [7, 21, 3]
nums = [5, 2, 6, 2]
nums = [10, 5, 9, 3, 15]
print(Solution().gcdSort(nums))
