class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        mem = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        res = 0

        for c in croakOfFrogs:
            if c not in mem:
                return -1
            mem[c] += 1
            # print(c,mem)

            if mem['c'] < mem['r'] or mem['r'] < mem['o'] or \
                    mem['o'] < mem[ 'a'] or mem['a'] < mem['k']:
                return -1
            res = max(res, max(mem.values()) - min(mem.values()))

        if max(mem.values()) - min(mem.values()) != 0:
            return -1

        return res


croakOfFrogs = "croakcroak"
croakOfFrogs = "crcoakroak"
croakOfFrogs = "croakcrook"
croakOfFrogs = "aoocrrackk"
croakOfFrogs = "araarcokocokckr"
print(Solution().minNumberOfFrogs(croakOfFrogs))
