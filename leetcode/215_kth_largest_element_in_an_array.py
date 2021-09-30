from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random

        random.shuffle(nums)

        t = k-1
        lo, hi = 0, len(nums)-1

        while lo < hi:
            j = self.partition(nums, lo, hi)
            if j > t:
                hi = j-1
            elif j < t:
                lo = j+1
            else:
                return nums[t]

        return nums[t]

    def partition(self, nums: list[int], lo: int, hi: int) -> int:
        i, j = lo+1, hi

        while True:
            while nums[i] > nums[lo]:
                if i == hi:
                    break
                i += 1
            while nums[j] < nums[lo]:
                j -= 1

            if i >= j:
                break

            self.exchange(nums, i, j)
            i += 1
            j -= 1

        self.exchange(nums, lo, j)

        return j

    def exchange(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


if __name__ == '__main__':
    # given an array of integers,
    # return the kth largest number in that array

    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    solution = Solution()
    ans = solution.findKthLargest(nums, k)

    assert ans == 5, f'ans={ans}'
