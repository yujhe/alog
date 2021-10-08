class Solution:
    def numDecodings(self, s: str) -> int:
        # the idea of finding decoding ways: m[i] = m[i-1] + m[i-2]
        # and there are some cases you have to take case
        # case 1: number of i and i-1 between 10~26
        #   m[i] = m[i-1] + m[i-2]
        # case 2: number of i and i-1 larger than 26
        #   m[i] = m[i-1]
        # case 3: number of i == 0 and i-1 == 1 or i-1 == 2
        #   m[i] = m[i-2]
        # case 4: number of i == 0 and i-1 > 2
        #   return 0

        if s[0] == '0':
            return 0

        m = [0] * (len(s)+1)
        m[0] = 1  # empty string
        m[1] = 1  # first digit

        for i in range(2, len(s)+1):
            if s[i-1] == '0':
                if s[i-2] in '12':
                    m[i] = m[i-2]
                else:
                    return 0
            else:
                m[i] = m[i-1]
                if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] in '0123456'):
                    m[i] += m[i-2]

        return m[-1]

        # another solution using two variables
        # cur=1 means we take s[0]
        # prev=1 means we take nothing
        #
        # prev, cur = 1, 1
        # for i in range(1, len(s)):
        #     c = 0
        #     if s[i] != '0':
        #         c = cur

        #     # digits between 10~26
        #     if s[i-1] == '1' or (s[i-1] == '2' and s[i] in '0123456'):
        #         c += prev

        #     prev = cur
        #     cur = c

        # return cur


if __name__ == '__main__':
    # given an encoded string
    # 'A' -> "1"
    # 'B' -> "2"
    # ...
    # 'Z' -> "26"
    # return the possible way to decode it

    s = "226"

    solution = Solution()
    ans = solution.numDecodings(s)

    assert ans == 3, f'ans={ans}'
