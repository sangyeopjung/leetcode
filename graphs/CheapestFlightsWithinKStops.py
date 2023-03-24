# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# tags: dp, shortest path, bfs

# O(N + Eklog(Ek))
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for frm, to, price in flights:
            adj[frm].append((to, price))
        
        heap = [(0, -1, src)]
        visited = [float('inf') for _ in range(n)]
        while heap:
            cost, num_stops, stop = heappop(heap)
            if stop == dst:
                return cost
            if num_stops >= visited[stop] or num_stops == k:
                continue
            visited[stop] = num_stops
            for neighbour, price in adj[stop]:
                heappush(heap, (cost + price, num_stops + 1, neighbour))

        return -1
    


# O((N + E)k)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford
        cost = [float('inf') for _ in range(n)]
        cost[src] = 0
        for _ in range(k+1):
            tmp = cost.copy()
            for frm, to, price in flights:
                tmp[to] = min(tmp[to], cost[frm] + price)
            cost = tmp
        
        return -1 if cost[dst] == float('inf') else cost[dst]
