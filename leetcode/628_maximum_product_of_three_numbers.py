from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])


if __name__ == '__main__':
    # Given an integer array nums,
    # find three numbers whose product is maximum and return the maximum product.

    nums = [1, 2, 3]

    solution = Solution()
    ans = solution.maximumProduct(nums)

    assert ans == 6, f'ans={ans}'
