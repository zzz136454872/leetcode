from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)

        if end not in bank:
            return -1
        bank.discard(end)
        bank.discard(start)
        bank = list(bank)
        bank.insert(0, start)
        bank.append(end)

        def near(a, b):
            tmp = 0

            for i in range(len(a)):
                if a[i] != b[i]:
                    tmp += 1

                    if tmp > 1:
                        return False

            return True

        adj = [[] for i in range(len(bank))]

        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                if near(bank[i], bank[j]):
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [False] * len(bank)
        visited[0] = True
        queue = [(0, 0)]

        while len(queue) > 0:
            now = queue.pop(0)

            if now[0] == len(bank) - 1:
                return now[1]

            for nxt in adj[now[0]]:
                if not visited[nxt]:
                    queue.append((nxt, now[1] + 1))

        return -1


start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
print(Solution().minMutation(start, end, bank))
