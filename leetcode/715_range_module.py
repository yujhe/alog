class RangeModule:

    def __init__(self):
        self.ranges = []

    # get the index of boundaries
    # lo: range[1] >= left
    # hi: range[0] <= right
    def get_boundaries(self, left: int, right: int) -> tuple[int, int]:
        lo, hi = 0, len(self.ranges)-1

        while lo < len(self.ranges) and self.ranges[lo][1] < left:
            lo += 1
        while hi >= 0 and self.ranges[hi][0] > right:
            hi -= 1

        return (lo, hi)

    # Adds the half-open interval [left, right), tracking every real number in that interval
    def addRange(self, left: int, right: int) -> None:
        lo, hi = self.get_boundaries(left, right)

        # merge the overlap intervals
        if lo <= hi:
            left = min(left, self.ranges[lo][0])
            right = max(right, self.ranges[hi][1])

        self.ranges[lo:hi+1] = [(left, right)]

    # Returns true if every real number in the interval [left, right) is currently being tracked,
    # and false otherwise.
    def queryRange(self, left: int, right: int) -> bool:
        lo, hi = self.get_boundaries(left, right)
        return lo == hi and self.ranges[lo][0] <= left and self.ranges[lo][1] >= right

    #  Stops tracking every real number currently being tracked in the half-open interval [left, right).
    def removeRange(self, left: int, right: int) -> None:
        lo, hi = self.get_boundaries(left, right)

        ranges = []
        if lo < len(self.ranges) and self.ranges[lo][0] < left:
            ranges.append((self.ranges[lo][0], left))
        if hi >= 0 and self.ranges[hi][1] > right:
            ranges.append((right, self.ranges[hi][1]))

        self.ranges[lo:hi+1] = ranges


if __name__ == '__main__':
    # Design a data structure to track the ranges represented as half-open intervals and query about them.
    # A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

    rangeModule = RangeModule()
    rangeModule.addRange(10, 180)
    rangeModule.addRange(150, 200)
    rangeModule.addRange(250, 500)
    assert rangeModule.queryRange(50, 100) == True
    assert rangeModule.queryRange(180, 300) == False
    assert rangeModule.queryRange(600, 1000) == False
    rangeModule.removeRange(50, 150)
    assert rangeModule.queryRange(50, 100) == False
