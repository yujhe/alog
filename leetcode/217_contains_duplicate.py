from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d:
                return True
            else:
                d[num] = num
        return False


if __name__ == '__main__':
    # given an array of integers,
    # return true if the array contains duplicate numbers
    nums = [1, 2, 3, 1]

    solution = Solution()

    assert solution.containsDuplicate(nums) == True
