from typing import List


class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        eps = 10**(-9)
        sizes = [len(doc) for doc in docs]

        for i in range(len(docs)):
            docs[i] = set(docs[i])
        mem = {}

        for i, doc in enumerate(docs):
            for num in doc:
                if num in mem:
                    mem[num].add(i)
                else:
                    mem[num] = {i}
        out = []

        for i, doc in enumerate(docs):
            log = [0] * 500

            for num in doc:
                for j in mem[num]:
                    if j > i:
                        log[j] += 1

            for k in range(i + 1, len(docs)):
                if log[k] > 0:
                    sim = log[k] / (sizes[i] + sizes[k] - log[k]) + eps
                    out.append(
                        str(i) + ',' + str(k) + ': ' + '{:.4f}'.format(sim))

        return out


sl = Solution()
inp = [[14, 15, 100, 9, 3], [32, 1, 9, 3, 5], [15, 29, 2, 6, 8, 7], [7, 10]]
print(sl.computeSimilarities(inp))
