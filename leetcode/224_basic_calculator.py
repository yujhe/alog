class Solution:
    def calculate(self, s: str) -> int:
        signs = {'+': 1, '-': -1}

        stack = []
        cur_num, cur_sign = 0, 1

        rs = 0

        for c in s:
            if c.isdigit():
                cur_num = cur_num*10 + int(c)
            elif c != ' ':
                if c in signs:
                    rs += cur_sign * cur_num
                    cur_sign = signs[c]
                elif c == '(':
                    stack.append((rs, cur_sign))
                    rs, cur_sign = 0, 1
                elif c == ')':
                    rs += cur_sign * cur_num
                    prev_rs, prev_sign = stack.pop()
                    rs = prev_rs + prev_sign*rs

                cur_num = 0

        return rs + cur_sign * cur_num


if __name__ == '__main__':
    # given a string representing a valid expression,
    # implement a basic calculator to evaluate it
    # return the result of calculation

    s = "1 + 1"

    solution = Solution()
    ans = solution.calculate(s)

    assert ans == 2, f'ans={ans}'
