from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for n in nums:
            sum += n

        n = len(nums)

        return int((1+n)*n/2 - sum)


if __name__ == '__main__':
    # given an array of n distinct numbers in [0, n]
    # return the missing number in the array
    nums = [3, 0, 1]

    solution = Solution()

    assert solution.missingNumber(nums) == 2
