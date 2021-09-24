from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # use prefix sum to find out the max sum
        max_sum, min_sum = nums[0], 0
        prefix_sum = 0

        for n in nums:
            prefix_sum += n
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum


if __name__ == '__main__':
    # given an integer array,
    # find the largest sum in a contiguous array

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    solution = Solution()
    ans = solution.maxSubArray(nums)

    assert ans == 6, f'ans={ans}'
