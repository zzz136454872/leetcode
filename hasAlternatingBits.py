class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        mem = set([
            1, 2, 5, 10, 21, 42, 85, 170, 341, 682, 1365, 2730, 5461, 10922,
            21845, 43690, 87381, 174762, 349525, 699050, 1398101, 2796202,
            5592405, 11184810, 22369621, 44739242, 89478485, 178956970,
            357913941, 715827882, 1431655765, 2863311530
        ])
        # for i in range(32):
        #     tmp=0
        #     for j in range(i,-1,-2):
        #         tmp|=(1<<j)
        #     mem.add(tmp)
        # print(sorted(list(mem)))

        return n in mem


n = 5
print(Solution().hasAlternatingBits(n))
