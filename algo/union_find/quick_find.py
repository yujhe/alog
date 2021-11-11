class QuickFind:
    def __init__(self, n: int):
        self.n = n
        self.id = list(range(n))
        self.num_components = n

    def find(self, p: int) -> int:
        return self.id[p]

    def union(self, p: int, q: int) -> None:
        p_id, q_id = self.id[p], self.id[q]
        if p_id != q_id:
            for i in range(self.n):
                if self.id[i] == p_id:
                    self.id[i] = q_id
            self.num_components -= 1

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def count(self) -> int:
        return self.num_components


if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        n = int(fin.readline())
        print(f'n={n}')

        uf = QuickFind(n)

        for line in fin:
            nodes = [int(i) for i in line.strip().split()]
            p, q = nodes[0], nodes[1]

            print(f'connect ({p}, {q})')
            if uf.connected(p, q):
                print(f'p={p}, q={q} is already connected')
            else:
                uf.union(p, q)

        connected_components = uf.count()
        assert connected_components == 2, f'# of components = {connected_components}'
