class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        t1 = current.split(':')
        t2 = correct.split(':')
        t1 = list(map(int, t1))
        t2 = list(map(int, t2))
        diff = 60 * t2[0] - t1[0] * 60 + t2[1] - t1[1]
        out = 0

        while diff >= 60:
            out += 1
            diff -= 60

        while diff >= 15:
            out += 1
            diff -= 15

        while diff >= 5:
            out += 1
            diff -= 5
        out += diff

        return out


current = "02:30"
correct = "04:35"
current = "11:00"
correct = "11:01"
print(Solution().convertTime(current, correct))
