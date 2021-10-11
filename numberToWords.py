class Solution:
    def numberToWords(self, num: int) -> str:
        table1 = [
            'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
            'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
            'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]
        table10 = [
            '', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
            'Seventy', 'Eighty', 'Ninety'
        ]
        tablek = ['', 'Thousand', 'Million', 'Billion']

        def f1000(a):
            out = []
            hunderd = a // 100

            if hunderd >= 1:
                out.append(table1[hunderd])
                out.append("Hundred")
            a -= 100 * hunderd

            if a < 20 and a > 0:
                out.append(table1[a])
            elif a >= 20:
                out.append(table10[a // 10])

                if a % 10 > 0:
                    out.append(table1[a % 10])

            return out

        out = []

        if num == 0:
            return 'Zero'
        base = 0

        while num > 0:
            a = num % 1000
            num = num // 1000
            tmp = f1000(a)

            if base > 0 and len(tmp) > 0:
                tmp.append(tablek[base])
            out = tmp + out
            base += 1

        return ' '.join(out)


sl = Solution()
num = 1000000
print(sl.numberToWords(num))
