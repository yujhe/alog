class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


if __name__ == '__main__':
    input = ('anagram', 'nagaram')

    print(f'input: {input}')
    print(f'output: {Solution().isAnagram(input[0], input[1])}')
