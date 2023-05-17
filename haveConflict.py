from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def parse(t):
            t = t.split(':')

            return 60 * int(t[0]) + int(t[1])

        t10 = parse(event1[0])
        t11 = parse(event1[1])
        t20 = parse(event2[0])
        t21 = parse(event2[1])

        return not (t11 < t20 or t21 < t10)


event1 = ["01:15", "02:00"]
event2 = ["02:00", "03:00"]
event1 = ["01:00", "02:00"]
event2 = ["01:20", "03:00"]
event1 = ["10:00", "11:00"]
event2 = ["14:00", "15:00"]
print(Solution().haveConflict(event1, event2))
