from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # move the index of shorter y to higher y
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            w = right - left
            h = min(height[left], height[right])

            max_area = max(max_area, w*h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    # given n non-negative integers, a1, a2, ..., an
    # each present a vertical line in (n, 0)~(n, an)
    # return the max area that formed by two line with x-axis
    #
    # Input: height = [1,8,6,2,5,4,8,3,7]
    # Output: 49
    # Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
    # In this case, the max area of water (blue section) the container can contain is 49.

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    solution = Solution()

    assert solution.maxArea(
        height) == 49, f'max area={solution.maxArea(height)}'
