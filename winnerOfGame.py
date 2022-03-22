from typing import List


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        acount = 0
        bcount = 0
        count = 0
        flag = 'c'

        for letter in colors:
            if letter == flag:
                count += 1
            else:
                if count >= 3:
                    if flag == 'A':
                        acount += count - 2
                    else:
                        bcount += count - 2
                flag = letter
                count = 1

        if count >= 3:
            if flag == 'A':
                acount += count - 2
            else:
                bcount += count - 2
        # print(acount,bcount)

        if acount > bcount:
            return True

        return False


colors = "AAABABB"
# colors = "AA"
# colors = "ABBBBBBBAAA"
print(Solution().winnerOfGame(colors))
