class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        mask = 1

        for _ in range(32):
            digit = n & mask
            m = m << 1
            if digit > 0:
                m += 1
            mask = mask << 1

        return m


if __name__ == '__main__':
    # Reverse bits of a given 32 bits unsigned integer

    pass
