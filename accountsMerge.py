from typing import *

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        logs={}
        class AC():
            def __init__(self):
                self.name=None
                self.emails=set()

        for account in accounts:
            a=set()
            for email in account[1:]:
                if email in logs.keys():
                    a.add(logs[email])
            if len(a)==0:
                log=AC()
                log.name=account[0]
                for email in account[1:]:
                    log.emails.add(email)
                    logs[email]=log
            elif len(a)==1:
                log=a.pop()
                for email in account[1:]:
                    log.emails.add(email)
                    logs[email]=log
            else:
                # 多个合并
                log=a.pop()
                while len(a)>0:
                    new_log=a.pop()
                    log.emails|=new_log.emails
                for email in account[1:]:
                    log.emails.add(email)
                for email in log.emails:
                    logs[email]=log
        vs=set(logs.values())
        out=[]
        for v in vs:
            out.append([v.name]+sorted(list(v.emails)))
        return out

sl=Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

print(sl.accountsMerge(accounts))

