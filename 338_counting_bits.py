from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # count(n) = count(2*n)
        # count(2*n+1) = count(n)+1

        count = [0]

        for i in range(1, n+1):
            count.append(count[i//2] + i % 2)

        return count


if __name__ == '__main__':
    # given n, return an array of n+1
    # arr[i] =  # of 1's in binary representation

    # Input: n = 2
    # Output: [0,1,1]
    # Explanation:
    # 0 --> 0
    # 1 --> 1
    # 2 --> 10

    solution = Solution()

    assert solution.countBits(2) == [0, 1, 1]
    assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
