from typing import List


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        print(dominoes)
        ldis = [12345] * n
        rdis = [12345] * n
        dom = list(dominoes)

        for i in range(n):
            if dominoes[i] == 'R':
                ldis[i] = 0
            elif dominoes[i] == 'L':
                continue
            elif i > 0 and ldis[i - 1] < 12345:
                ldis[i] = ldis[i - 1] + 1

        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                rdis[i] = 0
            elif dominoes[i] == 'R':
                continue
            elif i < n - 1 and rdis[i + 1] < 12345:
                rdis[i] = rdis[i + 1] + 1

        for i in range(n):
            if ldis[i] == '0' or rdis[i] == '0' or ldis[i] == rdis[i]:
                continue

            if ldis[i] < rdis[i]:
                dom[i] = 'R'
            else:
                dom[i] = 'L'

        return ''.join(dom)


dominoes = "RR.L"
dominoes = ".L.R...LR..L.."
print(Solution().pushDominoes(dominoes))
