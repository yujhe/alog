from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start time
        intervals.sort()

        if len(intervals) == 0:
            return 0

        count = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            if s < prev_end:
                count += 1
                prev_end = min(e, prev_end)
            else:
                prev_end = e

        return count


class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time
        intervals.sort(key=lambda p: p[1])

        if len(intervals) == 0:
            return 0

        count = 0
        prev_e = intervals[0][1]
        for i in range(1, len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            if s < prev_e:
                count += 1
            else:
                prev_e = e

        return count


if __name__ == '__main__':
    # given an array of intervals, interval[i] = [start i, end i]
    # return the minimum intervals you need to delete to get a non-overlaping intervals
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

    solution = Solution()
    ans = solution.eraseOverlapIntervals(intervals)

    assert ans == 1, f'ans={ans}'
