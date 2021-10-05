from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, not_rob = 0, 0

        for num in nums:
            rob_this = not_rob + num
            not_rob_this = max(rob, not_rob)
            rob = rob_this
            not_rob = not_rob_this

        return max(rob, not_rob)


if __name__ == '__main__':
    # given an integer array
    # return the maximum sum that you can't take numbers in adjacent

    nums = [1, 2, 3, 1]

    solution = Solution()
    ans = solution.rob(nums)

    assert ans == 4, f'ans={ans}'
