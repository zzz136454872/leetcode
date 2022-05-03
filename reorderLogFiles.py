from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        number = []
        alpha = []

        for log in logs:
            log = (log.split(), log)

            if log[0][1].isalpha():
                alpha.append(log)
            else:
                number.append(log)
        alpha.sort(key=lambda x: x[0][1:] + [x[0][0]])

        return [x[1] for x in alpha + number]


logs = [
    "dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig",
    "let3 art zero"
]
logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
print(Solution().reorderLogFiles(logs))
