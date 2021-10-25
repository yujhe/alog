class Solution:
    def findIntegers(self, n: int) -> int:
        # 1 bit: 0, 1
        # 2 bits: 0[0, 1], 1[0]
        # 3 bits: 0[xx], 10[x] = 2 bits + 1 bit
        # we can get # of integers that not contains '11' by
        # dp[i] = dp[i-1] + dp[i-2], i is the # of bits

        dp = [0] * 32  # total 32 bits
        dp[0] = 1  # 0 bit
        dp[1] = 2  # 1 bit

        for i in range(2, 32):
            dp[i] = dp[i-1] + dp[i-2]

        k = 31  # max number of mask (k=0 -> 1, k=1 -> 10, k=2 -> 100)
        prev_bit = 0  # previous bit
        n_is_valid = True  # number n not contains '11'
        count = 0
        while k >= 0:
            if n & (1 << k) > 0:
                count += dp[k]
                if prev_bit == 1:
                    # if the previous bit is '1', we run into the case '1(1xxx)'
                    # we don't need to run into the case > '1(1000)'
                    # and the number n is an invalid number
                    n_is_valid = False
                    break
                else:
                    prev_bit = 1
            else:
                prev_bit = 0
            k -= 1

        return count + 1 if n_is_valid else count


if __name__ == '__main__':
    # given an integer n,
    # return the number of the integers in the range [0, n]
    # whose binary representations do not contain consecutive ones.

    n = 5

    solution = Solution()
    ans = solution.findIntegers(n)

    assert ans == 5, f'ans={ans}'
