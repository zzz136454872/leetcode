class Solution:
    def magicalString(self, n: int) -> int:
        mem = [1, 2, 2]
        i = 2
        flag = 1

        while len(mem) < n:
            for j in range(mem[i]):
                mem.append(flag)
            flag = 3 - flag
            i += 1
        # print(mem)

        return mem[:n].count(1)


n = 6
n = 1
print(Solution().magicalString(n))
