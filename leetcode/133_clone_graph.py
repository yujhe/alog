from typing import Deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None

        cloned = {node: Node(node.val)}

        q = Deque()
        q.appendleft(node)

        while q:
            n = q.pop()
            for v in n.neighbors:
                if v not in cloned:
                    cloned[v] = Node(v.val)
                    q.appendleft(v)
                cloned[n].neighbors.append(cloned[v])

        return cloned[node]


if __name__ == '__main__':
    # given a node,
    # return a cloned graph

    pass
