class Solution:
    def maskPII(self, S: str) -> str:
        if '@' in S:
            return self.transMail(S)
        else:
            return self.transPhone(S)

    def transMail(self, S):
        S = S.lower()
        loc = S.index('@')
        front = S[:loc]
        back = S[loc:]
        front = front[0] + '*****' + front[-1]

        return front + back

    def transPhone(self, S):
        S = S.replace('(', '')
        S = S.replace(')', '')
        S = S.replace('-', '')
        S = S.replace('+', '')
        S = S.replace(' ', '')
        front = ''

        if len(S) > 10:
            front = '+' + '*' * (len(S) - 10) + '-'
        S = front + '***-***-' + S[-4:]

        return S


sl = Solution()
phone = "86-(10)12345678"
mail = 'AB@qq.com'
print(sl.maskPII(phone))
print(sl.maskPII(mail))
