from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        n = []
        for idx, interval in enumerate(intervals):
            if idx == 0:
                n.append(interval)
                continue

            s, e = interval[0], interval[1]
            prev_s, prev_e = n[-1][0], n[-1][1]
            if s <= prev_e:
                n[-1] = [prev_s, max(e, prev_e)]
            else:
                n.append(interval)

        return n


if __name__ == '__main__':
    input = [[1, 4], [2, 3]]

    print(f'input: {input}')
    print(f'output: {Solution().merge(input)}')
