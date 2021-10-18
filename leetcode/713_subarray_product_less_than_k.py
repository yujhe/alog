from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # use sliding window to find all possible solution
        # iterate nums and move left if the product >= k
        prod = 1
        l = 0
        rs = 0

        for r in range(len(nums)):
            prod *= nums[r]

            # move left if current product >= k
            while prod >= k:
                if l > r:
                    break
                prod /= nums[l]
                l += 1

            # possible solution that contains nums[r]
            rs += r - l + 1

        return rs


if __name__ == '__main__':
    # Given an array of integers nums and an integer k,
    # return the number of contiguous subarrays
    # where the product of all the elements in the subarray is strictly less than k.

    nums = [10, 5, 2, 6]
    k = 100

    solution = Solution()
    ans = solution.numSubarrayProductLessThanK(nums, k)

    assert ans == 8, f'ans={ans}'
