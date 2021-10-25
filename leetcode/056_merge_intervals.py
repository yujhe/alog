from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        s, e = intervals[0][0], intervals[0][1]
        merged = []

        for interval in intervals:
            if self.is_overlapped([s, e], interval):
                s = min(s, interval[0])
                e = max(e, interval[1])
            else:
                merged.append([s, e])
                s, e = interval[0], interval[1]
        merged.append([s, e])

        return merged

    def is_overlapped(self, v1: tuple[int, int], v2: tuple[int, int]) -> bool:
        return v1[0] <= v2[0] <= v1[1] or v1[0] <= v2[1] <= v1[1]


if __name__ == '__main__':
    # Given an array of intervals where intervals[i] = [starti, endi],
    # merge all overlapping intervals,
    # and return an array of the non-overlapping intervals that cover all the intervals in the input.

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    solution = Solution()
    ans = solution.merge(intervals)

    assert ans == [[1, 6], [8, 10], [15, 18]], f'ans={ans}'
