from typing import List


class Node:
    def __init__(self, domain, parent):
        self.domain = domain
        self.parent = parent
        self.children = {}
        self.count = 0


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        root = Node("", None)

        for d in cpdomains:
            count, domain = d.split()
            count = int(count)
            domain = domain.split('.')
            p = root

            for dm in domain[::-1]:
                if dm not in p.children:
                    p.children[dm] = Node(dm, p)
                p = p.children[dm]
                p.count += count
        # print(root)

        s = []
        res = []

        def travel(r):
            s.append(r.domain)
            res.append(str(r.count) + ' ' + '.'.join(s[len(s) - 1:0:-1]))

            for nxt in r.children.values():
                travel(nxt)
            s.pop()

        travel(root)

        return res[1:]


cpdomains = ["9001 discuss.leetcode.com"]
cpdomains = [
    "900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"
]

print(Solution().subdomainVisits(cpdomains))
