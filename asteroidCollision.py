from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if len(stack) == 0 or stack[-1] < 0 or a > 0:
                stack.append(a)

                continue
            flag = True

            while len(stack) > 0 and stack[-1] > 0:
                if stack[-1] > -a:
                    flag = False

                    break
                tmp = stack.pop()

                if tmp == -a:
                    flag = False

                    break

            if flag:
                stack.append(a)

        return stack


asteroids = [5, 10, -5]
asteroids = [10, 2, -5]
asteroids = [-2, -2, 1, -2]
print(Solution().asteroidCollision(asteroids))
