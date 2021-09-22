from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}  # num -> frequency
        for num in nums:
            m[num] = m.get(num, 0) + 1

        # use quick select to find kth most frequent numbers
        items = list(m.items())
        idx = self.select(items, len(m) - k)

        topk = [i[0] for i in items[idx:]]

        return topk

    def less(self, p, q):
        return p < q

    def exchange(self, a, p, q):
        temp = a[p]
        a[p] = a[q]
        a[q] = temp

    def partition(self, a, lo, hi) -> int:
        i, j = lo+1, hi
        while True:
            while self.less(a[i][1], a[lo][1]):
                if i == hi:
                    break
                i += 1
            while self.less(a[lo][1], a[j][1]):
                j -= 1

            if i >= j:
                break

            self.exchange(a, i, j)
            i += 1
            j -= 1

        self.exchange(a, lo, j)

        return j

    def select(self, a, k) -> int:
        lo, hi = 0, len(a) - 1
        while lo < hi:
            j = self.partition(a, lo, hi)
            if k < j:
                hi = j-1
            elif k > j:
                lo = j+1
            else:
                return k
        return k


if __name__ == '__main__':
    # given an array of integers,
    # return the kth most frequent item in any order

    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    solution = Solution()

    assert Counter(solution.topKFrequent(nums, k)) == Counter(
        [1, 2]), f'output={solution.topKFrequent(nums, k)}'
