from Iterator import Iterator


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked = False
        self.peekedValue = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """

        if not self.peeked:
            self.peekedValue = self.iterator.next()
            self.peeked = True

        return self.peekedValue

    def next(self):
        """
        :rtype: int
        """

        if self.peeked:
            self.peeked = False

            return self.peekedValue

        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """

        if self.peeked or self.iterator.hasNext():
            return True

        return False
