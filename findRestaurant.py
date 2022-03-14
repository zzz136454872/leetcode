from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)

        def key(x):
            return list1.index(x) + list2.index(x)

        mk = min(key(x) for x in common)

        return list(filter(lambda x: key(x) == mk, common))


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = [
    "Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"
]
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]

print(Solution().findRestaurant(list1, list2))
