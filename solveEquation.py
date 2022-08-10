class Solution:
    def solveEquation(self, equation: str) -> str:
        left = [0, 0]
        right = [0, 0]
        leftPart = True
        sign = 1
        tmp = 0
        prev = ''

        for letter in equation:
            if letter.isdigit():
                tmp = tmp * 10 + int(letter)
                prev = letter

                continue

            if letter == 'x':
                if tmp == 0 and prev != '0':
                    tmp = 1

                if leftPart:
                    left[0] += sign * tmp
                else:
                    right[0] += sign * tmp
                sign = 1
                tmp = 0
                prev = letter

                continue

            if leftPart:
                left[1] += sign * tmp
            else:
                right[1] += sign * tmp
            sign = 1
            tmp = 0

            if letter == '=':
                leftPart = False
            elif letter == '-':
                sign = -1
            prev = letter

        right[1] += sign * tmp
        print(left, right)

        if left[0] == right[0]:
            if left[1] == right[1]:
                return "Infinite solutions"

            return "No solution"

        return "x=" + str((right[1] - left[1]) // (left[0] - right[0]))


equation = "x+5-3+x=6+x-2"
equation = "x=x"
equation = "2x=x"
equation = "0x=0"
equation = "1-x+x-x+x=99"
print(Solution().solveEquation(equation))
