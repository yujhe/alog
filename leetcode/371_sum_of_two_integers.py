class Solution:
    def getSum(self, a: int, b: int) -> int:
        # use bit operation

        mask = 0xffffffff  # mask for 32-bit

        while b & mask > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # handle overflow. (a & mask) = a
        return (a & mask) if b > 0 else a


if __name__ == '__main__':
    # given two integers,
    # return the sum of them without using '+' or '-'

    a = 1
    b = 2

    solution = Solution()
    ans = solution.getSum(a, b)

    assert ans == 3, f'ans={ans}'
