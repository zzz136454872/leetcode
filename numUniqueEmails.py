from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mem = set()

        for email in emails:
            tmp = ''
            getAt = False
            getAdd = False

            for letter in email:
                if getAt:
                    tmp += letter

                    continue

                if letter == '@':
                    getAt = True
                    tmp += letter

                    continue

                if getAdd:
                    continue

                if letter == '.':
                    continue

                if letter == '+':
                    getAdd = True

                    continue
                tmp += letter
            mem.add(tmp)
        print(mem)

        return len(mem)


emails = [
    "test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]
emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]

print(Solution().numUniqueEmails(emails))
