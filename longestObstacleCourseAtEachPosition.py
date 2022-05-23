from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self,
                                            obstacles: List[int]) -> List[int]:
        d = [obstacles[0]]
        res = [1]

        for ob in obstacles[1:]:
            if ob >= d[-1]:
                d.append(ob)
                res.append(len(d))
            else:
                left = 0
                right = len(d) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if d[mid] <= ob:
                        left = mid + 1
                    else:
                        right = mid - 1
                res.append(left + 1)
                d[left] = ob

        return res


obstacles = [1, 2, 3, 2]
print(Solution().longestObstacleCourseAtEachPosition(obstacles))
