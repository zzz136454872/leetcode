from bisect import bisect_right
from collections import defaultdict
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
class Solution2:
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


# deliciousness = [1, 3, 5, 7, 9]
# deliciousness = [1, 1, 1, 3, 3, 3, 7]
# sl = Solution()
# print(sl.countPairs(deliciousness))


# 1782. 统计点对的数目
class Solution:
    def countPairs(self, n: int, edges: List[List[int]],
                   queries: List[int]) -> List[int]:
        adjList = defaultdict(lambda: defaultdict(int))
        links = {i: 0 for i in range(n)}

        for a, b in edges:
            a -= 1
            b -= 1
            adjList[a][b] += 1
            adjList[b][a] += 1
            links[a] += 1
            links[b] += 1
        mem = sorted([v for v in links.values()])

        # print('adj', adjList)
        # print('mem', mem)
        # print('link', links)

        res = []

        for q in queries:
            # print('query', q)
            r = 0

            for i in range(n):
                tmp = 0
                t = q - links[i]

                if links[i] > t:
                    tmp -= 1
                j = bisect_right(mem, t)
                tmp += n - j

                for b, v in adjList[i].items():
                    if links[b] > t and links[b] - v <= t:
                        tmp -= 1
                # print(i, j, tmp, t)
                r += tmp
            res.append(r // 2)

        return res


n = 4
edges = [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]]
queries = [2, 3]
print(Solution().countPairs(n, edges, queries))
