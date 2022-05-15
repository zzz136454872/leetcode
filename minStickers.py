from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        mem = {}

        for letter in target:
            mem[letter] = mem.get(letter, 0) + 1
        mem = sorted(mem.items())
        n = len(mem)
        locs = {mem[i][0]: i for i in range(n)}

        # print("locs",locs)
        def tosupply(word):
            mask = [0 for _ in range(n)]

            for letter in word:
                if letter in locs:
                    mask[locs[letter]] += 1

            return tuple(mask)

        ss = (tosupply(sticker) for sticker in stickers)
        ss = tuple(filter(lambda x: any(x), ss))
        # print('ss',ss)
        needs = tosupply(target)
        # print('needs',needs)
        mem = [{} for i in range(len(ss))]

        def sub(need, supply):
            return tuple(max(need[i] - supply[i], 0) for i in range(n))

        def equal(need1, need2):
            return all((need1[i] == need2[i] for i in range(n)))

        def dfs(need, left):
            orineed = need

            if not any(need):
                return 0

            if left >= len(ss):
                return 16

            if need in mem[left]:
                return mem[left][need]
            res = 16

            for i in range(16):
                prev = need
                res = min(res, dfs(need, left + 1) + i)
                need = sub(need, ss[left])

                if equal(need, prev):
                    break
            mem[left][orineed] = res
            # print(orineed,left,res)

            return res

        res = dfs(needs, 0)

        if res < 16:
            return res

        return -1


# stickers = ["with","example","science"]
# target = "thehat"
# stickers = ["notice","possible"]
# target = "basicbasic"
stickers = [
    "right", "ten", "year", "share", "period", "paper", "expect", "village",
    "home", "happen", "ring", "sat", "even", "afraid", "paint", "self",
    "range", "camp", "note", "read", "paragraph", "run", "basic", "fill",
    "week", "his", "star", "power", "any", "colony", "object", "free", "dark",
    "said", "chick", "true", "glad", "child", "room", "lost", "am", "cry",
    "quiet", "crease", "while", "race", "fun", "found", "dream", "once"
]
target = "materialhalf"
print(Solution().minStickers(stickers, target))
