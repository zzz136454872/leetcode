#  Below is the interface for Iterator, which is already defined for you.


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.idx = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

        return self.idx < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.idx += 1

        return self.nums[self.idx - 1]


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    iterator = Iterator(nums)

    while iterator.hasNext():
        print(iterator.next())
