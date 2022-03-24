from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        img1 = [[0] * len(img[0]) for i in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[0])):
                a = 1
                b = img[i][j]

                if j > 0:
                    a += 1
                    b += img[i][j - 1]

                if j < len(img[0]) - 1:
                    a += 1
                    b += img[i][j + 1]

                if i > 0:
                    a += 1
                    b += img[i - 1][j]

                    if j > 0:
                        a += 1
                        b += img[i - 1][j - 1]

                    if j < len(img[0]) - 1:
                        a += 1
                        b += img[i - 1][j + 1]

                if i < len(img) - 1:
                    a += 1
                    b += img[i + 1][j]

                    if j > 0:
                        a += 1
                        b += img[i + 1][j - 1]

                    if j < len(img[0]) - 1:
                        a += 1
                        b += img[i + 1][j + 1]

                img1[i][j] = b // a

        return img1


img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
print(Solution().imageSmoother(img))
