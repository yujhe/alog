class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []

        for d in path.split('/'):
            if d == '..':
                if s:
                    s.pop()
            elif d and d != '.':
                s.append(d)

        return '/' + '/'.join(s)


if __name__ == '__main__':
    # given an absolute path
    # return a simplified canonical path
    # a canoical path should have the following format:
    #  - start with '/'
    #  - any two directories are separated by a single slash '/'
    #  - path not end with a tailing '/'
    #  - path only contains directories on the path from the root directory (no '.' or '..')

    path = '/home/'

    solution = Solution()
    ans = solution.simplifyPath(path)

    assert ans == '/home', f'ans={ans}'
