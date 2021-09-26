from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            m = lo + (hi-lo)//2

            if nums[m] < nums[hi]:  # right is higher
                hi = m
            else:
                lo = m+1

        return nums[lo]


if __name__ == '__main__':
    # given a rotated sorted integer array
    # return the minimum number in that array in O(lg N)
    # rotate an array means a[0], a[1], ..., a[n] -> a[n], a[0], a[1], ..., a[n-1]
    #
    # Input: nums = [3,4,5,1,2]
    # Output: 1
    # Explanation: The original array was [1,2,3,4,5] rotated 3 times.

    nums = [3, 4, 5, 1, 2]

    solution = Solution()
    ans = solution.findMin(nums)

    assert ans == 1, f'ans={ans}'
