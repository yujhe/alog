from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # negative * negative = positive
        # so we need to track the max previous product and min previous product
        prev_max, prev_min = nums[0], nums[0]
        max_so_far = nums[0]

        for n in nums[1:]:
            cur_max = max(prev_max*n, prev_min*n, n)
            cur_min = max(prev_max*n, prev_min*n, n)
            prev_max = cur_max
            prev_min = cur_min
            max_so_far = max(max_so_far, cur_max)

        return max_so_far


if __name__ == '__main__':
    # given an integer array,
    # find a contiguous non-empty subarray within the array that has the largest product

    nums = [2, 3, -2, 4]

    solution = Solution()
    ans = solution.maxProduct(nums)

    assert ans == 6, f'ans={ans}'
