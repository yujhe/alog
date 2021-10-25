from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1

        for k in range(m+n-1, -1, -1):
            if i < 0:
                nums1[k] = nums2[j]
                j -= 1
            elif j < 0:
                break
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1


if __name__ == '__main__':
    # given two integer arrays nums1 and nums2,
    # sorted in non-decreasing order,
    # and two integers m and n,
    # representing the number of elements in nums1 and nums2 respectively.
    # Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3

    nums2 = [2, 5, 6]
    n = 3

    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    assert sorted(nums1) == nums1, f'nums1={nums1}'
