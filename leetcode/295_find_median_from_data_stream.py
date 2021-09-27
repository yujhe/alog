import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []  # the smaller half of nums (max-heap)
        self.right = []  # the larger half of nums (min-heap)

    def addNum(self, num: int) -> None:
        # ensure the size and order between two heap
        if len(self.left) == len(self.right):
            # python heap is min-heap, invert the number for max-heap
            # heap size: left (k), right (k -> k+1)
            n = heapq.heappushpop(self.left, -num)
            heapq.heappush(self.right, -n)
        else:
            # heap size: left (k -> k+1), right (k+1)
            n = heapq.heappushpop(self.right, num)
            heapq.heappush(self.left, -n)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return self.right[0]


if __name__ == '__main__':
    # return the median of the nums
    # For example, for arr = [2,3,4], the median is 3.
    # For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    finder = MedianFinder()
    finder.addNum(-1)
    finder.addNum(-2)

    median = finder.findMedian()
    assert median == (-1-2)/2, f'median={median}'

    finder.addNum(-3)

    median = finder.findMedian()
    assert median == -2, f'median={median}'
