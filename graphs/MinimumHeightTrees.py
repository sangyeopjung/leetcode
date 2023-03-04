# https://leetcode.com/problems/minimum-height-trees/description/
# tags: graph, bfs

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        out = set(node for node in range(n))

        adj = defaultdict(list)
        inorders = [0 for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            inorders[a] += 1
            inorders[b] += 1
        
        outer = [node for node in range(n) if inorders[node] == 1]
        while len(out) > 2:
            inner = []
            for node in outer:
                for neighbour in adj[node]:
                    inorders[neighbour] -= 1
                    if inorders[neighbour] == 1:
                        inner.append(neighbour)
                out.remove(node)
            outer = inner
        
        return list(out)