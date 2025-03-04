from functools import cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        ss=s
        l=len(s)

        @cache
        def f1(s,e):
            # print(s,e)
            if e<=s:
                return 0
            if ss[s]==ss[e]:
                return f1(s+1,e-1)
            return f1(s+1,e-1)+1

        @cache
        def f(s,t):
            # print(s,t)
            if t==1:
                return f1(s,l-1)
            res=1000
            for i in range(s,l-t+1):
                res=min(res,f1(s,i)+f(i+1,t-1))
            return res

        return f(0,k)

s = "abc"
k = 2
s = "aabbc"
k = 3
s = "leetcode"
k = 8

s = "fyhowoxzyrincxivwarjuwxrwealesxsimsepjdqsstfggjnjhilvrwwytbgsqbpnwjaojfnmiqiqnyzijfmvekgakefjaxryyml"
k = 32
print(Solution().palindromePartition(s,k))


