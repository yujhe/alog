class Solution:
    def hammingWeight(self, n: int) -> int:
        # use mask to execute AND operation
        count = 0
        mask = 1

        for _ in range(32):
            if n & mask != 0:
                count += 1
            mask = mask << 1

        return count


if __name__ == '__main__':
    # given an integer,
    # return # of 1's bit in binary

    n = 11

    solution = Solution()

    assert solution.hammingWeight(n) == 3
