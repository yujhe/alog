from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # iterate list,
        # if nums[i] != nums[nums[i]-1], swap(nums[i], nums[nums[i]-1]
        # ex: 4, 2, 1 -> 1, 2, 4
        # the missing positive = i+1, if nums[i] != i+1

        i = 0
        while i < len(nums):
            n = nums[i]

            if 0 < n <= len(nums) and n != nums[n-1]:
                # swap
                nums[i] = nums[n-1]
                nums[n-1] = n
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return len(nums)+1


if __name__ == '__main__':
    # given an unsorted integer array nums,
    # return the smallest missing positive integer

    nums = [3, 2, 1]

    solution = Solution()
    ans = solution.firstMissingPositive(nums)

    assert ans == 4, f'ans={ans}'
