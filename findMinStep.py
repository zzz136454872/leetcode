from typing import List


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        handhash = 0
        # 红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W'
        dic = {'R': 1, 'Y': 10, 'B': 100, 'G': 1000, 'W': 10000}

        for a in hand:
            handhash += dic[a]

        mem = {}

        def simpilify(s):
            while True:
                i = 0
                changed = False

                while i < len(s) - 2:
                    j = i + 1

                    while j < len(s) and s[i] == s[j]:
                        j += 1

                    if j - i >= 3:
                        s = s[:i] + s[j:]
                        changed = True
                    i += 1

                if not changed:
                    return s

        def dfs(bod, hh):
            if len(bod) == 0:
                return 0
            out = 10

            if (bod, hh) in mem:
                return mem[(bod, hh)]

            for i in range(len(bod)):
                # if i > 0 and bod[i]==bod[i-1]:
                #     continue

                for c in dic.keys():
                    color = dic[c]
                    choose = (hh % (10 * color)) // color

                    if choose == 0:
                        continue
                    out = min(
                        dfs(simpilify(bod[:i] + c + bod[i:]), hh - color) + 1,
                        out)
            mem[(bod, hh)] = out
            # print(bod,hh,out)

            return out

        out = dfs(board, handhash)

        if out < 10:
            return out

        return -1


board = "WRRBBW"
hand = "RB"
board = "WWBBWW"
hand = "B"
board = "WWRRBBWW"
hand = "WRBRW"
board = "G"
hand = "GGGGG"
board = "RBYYBBRRB"
hand = "YRBGB"
print(Solution().findMinStep(board, hand))
