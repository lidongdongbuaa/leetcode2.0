class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:  # corner case
            return None
        if not node.neighbors:
            return node.copy()

        res = new = Node(node.val)
        visit = []

        queue =deque([(node, new)])
        while queue:
            node, new = queue.popleft()
            visit.append(node)
            for elem in node.neighbors:
                if elem not in visit:
                    tmp = Node(elem.val)
                    new.neighbors.append(tmp)
                    queue.append([elem, tmp])

        return res

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.neighbors = [b, d]
b.neighbors = [a, c]
c.neighbors = [b, d]
d.neighbors = [a, c]

x = Solution()
print(x.cloneGraph(a).neighbors[1].val)