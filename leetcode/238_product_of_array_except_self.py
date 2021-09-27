from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # from left to right
        # output[i] = output[i-1] * nums[i-1]
        # nums = [1, 2, 3], output = [1, 1*1, 1*1*2]
        #
        # from right to left, update suffix
        # output = [1*suffix, 1*1*suffix, 1*1*2]

        n = len(nums)
        output = [1] * n
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * suffix
            suffix *= nums[i]

        return output


if __name__ == '__main__':
    # given an integer array,
    # return an array that output[i] = the product without a[i]
    # you can't use division
    nums = [1, 2, 3, 4]
    solution = Solution()

    assert solution.productExceptSelf(nums) == [
        24, 12, 8, 6], f'productExceptSelf(nums)={solution.productExceptSelf(nums)}'
