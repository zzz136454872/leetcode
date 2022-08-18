from typing import List


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s = [ord(a) - ord('a') for a in s]

        if k == 1:
            m = s

            for i in range(len(s)):
                m = m[1:] + [m[0]]

                if s > m:
                    s = m
        else:
            s.sort()

        return ''.join([chr(a + ord('a')) for a in s])


s = "cba"
k = 1
s = "baaca"
k = 3
s = "xitavoyjqiupzadbdyymyvuteolyeerecnuptghlzsynozeuuvteryojyokpufanyrqqmtgxhyycltlnusyeyyqygwupcaagtkuq"
k = 1
print(Solution().orderlyQueue(s, k))
