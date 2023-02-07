from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def pt(a):
            return int(a[:2]) * 60 + int(a[3:])

        mem = defaultdict(list)

        for name, time in zip(keyName, keyTime):
            mem[name].append(pt(time))

        res = []

        for name, ts in mem.items():
            if len(ts) <= 2:
                continue
            ts.sort()

            for i in range(len(ts) - 2):
                if ts[i + 2] - ts[i] <= 60:
                    res.append(name)

                    break

        return sorted(res)


keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
keyName = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"]
keyTime = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]
keyName = ["john", "john", "john"]
keyTime = ["23:58", "23:59", "00:01"]
keyName = ["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"]
keyTime = ["13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"]

print(Solution().alertNames(keyName, keyTime))
