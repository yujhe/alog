from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # iterate the nums and get the longest length from previous num
        # ex: nums=[10, 9, 2, 5, 3]
        # when i=3 (nums[i]=5), the longest length to i=3 is the maximum length of (max_len[0]+1, max_len[1]+1, max_len[2]+1)

        max_len = [1] * len(nums)  # default length is 1
        for i in range(len(nums)):
            for j in range(i):
                # update the max length when tail is larger
                if nums[i] > nums[j]:
                    max_len[i] = max(max_len[i], max_len[j]+1)

        # return the maximum length
        return max(max_len)


if __name__ == '__main__':
    # given an integer array,
    # return the # of longest increaasing subsequence
    # you can get a subsequence by deleting any items from the array (without changing the order)
    #
    # Input: nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    solution = Solution()
    ans = solution.lengthOfLIS(nums)

    assert ans == 4, f'ans={ans}'
