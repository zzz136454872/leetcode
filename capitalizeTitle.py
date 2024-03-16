class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()

        for i in range(len(title)):
            if len(title[i]) <= 2:
                title[i] = title[i].lower()
            else:
                tmp = list(title[i].lower())
                tmp[0] = tmp[0].upper()
                title[i] = ''.join(tmp)

        return ' '.join(title)


title = "capiTalIze tHe titLe"
print(Solution().capitalizeTitle(title))
