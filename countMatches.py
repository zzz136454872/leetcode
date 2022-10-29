from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str,
                     ruleValue: str) -> int:
        mem = {"type": 0, "color": 1, "name": 2}
        idx = mem[ruleKey]
        res = 0

        for item in items:
            if item[idx] == ruleValue:
                res += 1

        return res


items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
         ["phone", "gold", "iphone"]]
ruleKey = "color"
ruleValue = "silver"

items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"],
         ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(Solution().countMatches(items, ruleKey, ruleValue))
