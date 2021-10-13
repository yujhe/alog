from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # consider rob houses between 0~n-1, 1~n
        from_1st_rob, from_1st_not_rob = nums[0], 0
        from_2nd_rob, from_2nd_not_rob = 0, 0

        for n in nums[1:-1]:
            from_1st_rob, from_1st_not_rob = self.update(from_1st_rob, from_1st_not_rob, n)
            from_2nd_rob, from_2nd_not_rob = self.update(from_2nd_rob, from_2nd_not_rob, n)
        from_2nd_rob, from_2nd_not_rob = self.update(from_2nd_rob, from_2nd_not_rob, nums[-1])

        return max(from_1st_rob, from_1st_not_rob, from_2nd_rob, from_2nd_not_rob)

    def update(self, rob_prev: int, not_rob_prev: int, n: int) -> tuple[int, int]:
        rob_this = not_rob_prev + n
        not_rob_this = max(rob_prev, not_rob_prev)

        return rob_this, not_rob_this


if __name__ == '__main__':
    # givn an integer array
    # return the maximum sum that you can't take numbers in adjacent
    # p.s. the head and the tail are adjacent too

    nums = [1, 2, 3, 1]

    solution = Solution()
    ans = solution.rob(nums)

    assert ans == 4, f'ans={ans}'
