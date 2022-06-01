from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        mem = set()

        for word in words:
            for letter in word:
                mem.add(letter)
        mem = sorted(list(mem))
        gt = {a: set() for a in mem}

        def diff(a, b):
            for i in range(min(len(a), len(b))):
                if a[i] != b[i]:
                    gt[a[i]].add(b[i])

                    return True

            return len(a) <= len(b)

        for i in range(len(words) - 1):
            if not diff(words[i], words[i + 1]):
                return ""

        print(gt)

        visited = {a: False for a in mem}
        tmp = set()

        def dfs(a):
            # print(a,tmp,gt)

            if visited[a]:
                return True

            if a in tmp:
                return False
            tmp.add(a)
            tmp2 = set()

            for nxt in gt[a]:
                if not dfs(nxt):
                    return False
                tmp2 |= gt[nxt]
            gt[a] |= tmp2
            tmp.pop()
            visited[a] = True

            return True

        print(gt)

        for a in mem:
            if not dfs(a):
                return ""

        n = len(mem)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if mem[i] in gt[mem[j]]:
                    mem[i], mem[j] = mem[j], mem[i]

        return ''.join(mem)


words = ["wrt", "wrf", "er", "ett", "rftt"]
# words = ["ax","z",'x']
words = ["vlxpwiqbsg", "cpwqwqcd"]
print(Solution().alienOrder(words))
