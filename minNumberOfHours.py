from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int,
                         energy: List[int], experience: List[int]) -> int:
        diffEn = 0
        diffEx = 0
        en = initialEnergy
        ex = initialExperience

        for i in range(len(energy)):
            if en < energy[i] + 1:
                diffEn += energy[i] + 1 - en
                en = 1
            else:
                en -= energy[i]

            if ex < experience[i] + 1:
                diffEx += experience[i] + 1 - ex
                ex = 2 * experience[i] + 1
            else:
                ex += experience[i]

        return diffEn + diffEx


initialEnergy = 5
initialExperience = 3
energy = [1, 4, 3, 2]
experience = [2, 6, 3, 1]
initialEnergy = 2
initialExperience = 4
energy = [1]
experience = [3]
print(Solution().minNumberOfHours(initialEnergy, initialExperience, energy,
                                  experience))
