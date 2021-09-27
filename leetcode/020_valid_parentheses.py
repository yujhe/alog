class Solution:
    parentheses = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    def isValid(self, s: str) -> bool:
        if s == '':
            return True

        stack = []
        for c in s:
            if self.parentheses.get(c):  # push to stack if we got left parentheses
                stack.append(c)
            else:
                # check the top element in stack is right parentheses
                if len(stack) == 0 or self.parentheses[stack.pop()] != c:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    s = '()[]{}'

    print(f'input: s = {s}')
    print(f'output: {Solution().isValid(s)}')
