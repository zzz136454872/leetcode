def rand7():
    return 0


class Solution:
    def rand10(self) -> int:
        """
        :rtype: int
        """
        r = rand7()

        while r == 7:
            r = rand7()
        c = rand7()

        while c >= 6:
            c = rand7()

        return (r % 2) * 5 + c
