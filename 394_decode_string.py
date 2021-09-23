class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_out = ''
        num = 0

        for i in range(len(s)):
            c = s[i]

            if c.isdigit():
                # handle number more than 1 digit
                num = 10*num + int(c)
            elif c == '[':
                stack.append((num, cur_out))
                cur_out = ''
                num = 0
            elif c == ']':
                prev_num, prev_out = stack.pop()
                cur_out = prev_out + cur_out*prev_num
            else:
                cur_out += c

        return cur_out


if __name__ == '__main__':
    # given an encode string,
    # return the decoded string
    # ex: 3[a]2[b]=aaabb

    s = '3[a2[c]]'

    solution = Solution()

    assert solution.decodeString(
        s) == 'accaccacc', f'decoded string={solution.decodeString(s)}'
