from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        mem = {}
        res = []

        for name in names:
            if name not in mem:
                mem[name] = 1
                res.append(name)
            else:
                r = mem[name]

                while True:
                    t = name + '(' + str(r) + ')'

                    if t not in mem:
                        mem[t] = 1
                        mem[name] = r + 1
                        res.append(t)

                        break
                    r += 1

        return res


names = ["pes", "fifa", "gta", "pes(2019)"]
names = ["gta", "gta(1)", "gta", "avalon"]
names = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]
names = ["wano", "wano", "wano", "wano"]
names = ["kaido", "kaido(1)", "kaido", "kaido(1)"]
print(Solution().getFolderNames(names))
