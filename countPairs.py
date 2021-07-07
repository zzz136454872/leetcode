from typing import List


class TrieNode:
    def __init__(self):
        self.child = [None, None]
        self.cnt = 0


def insertTrie(root, N):
    for i in range(15, -1, -1):
        x = bool((N) & (1 << i))

        if (root.child[x] is None):
            root.child[x] = TrieNode()
        root.child[x].cnt += 1
        root = root.child[x]


def cntSmaller(root, N, K):
    cntPairs = 0

    for i in range(15, -1, -1):
        if (root is None):
            break
        x = bool(N & (1 << i))
        y = K & (1 << i)

        if (y != 0):
            if (root.child[x]):
                cntPairs += root.child[x].cnt
            root = root.child[1 - x]
        else:
            root = root.child[x]

    return cntPairs


def cntSmallerPairs(arr, K):
    root = TrieNode()
    cntPairs = 0

    for i in range(len(arr)):
        cntPairs += cntSmaller(root, arr[i], K)
        insertTrie(root, arr[i])

    return cntPairs


# 不知道是哪个题了
class Solution0:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        return cntSmallerPairs(nums, high + 1) - cntSmallerPairs(nums, low)


sl = Solution0()
nums = [1, 4, 2, 7]
low = 2
high = 6
print(sl.countPairs(nums, low, high))

print('now')


def A(n):
    if n <= 1:
        return 0

    return n * (n - 1)


# 大餐计数
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        log = {}
        mod = 10**9 + 7

        for d in deliciousness:
            log[d] = log.get(d, 0) + 1
        exp = [1 << i for i in range(22)]
        out = 0

        for d in log.keys():
            if d in exp:
                out = (out + A(log[d])) % (2 * mod)

            for t in exp:
                if d != t - d:
                    out = (out + log[d] * log.get(t - d, 0)) % (2 * mod)

        return out // 2


deliciousness = [1, 3, 5, 7, 9]
deliciousness = [1, 1, 1, 3, 3, 3, 7]
sl = Solution()
print(sl.countPairs(deliciousness))
