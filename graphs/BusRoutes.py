# https://leetcode.com/problems/bus-routes/description/
# tags: bfs, graph

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_routes = defaultdict(list)
        for i, stops in enumerate(routes):
            for stop in stops:
                stop_to_routes[stop].append(i)
        
        queue = deque([(source, 0)])
        visited = set()
        while queue:
            stop, n = queue.popleft()
            if stop == target:
                return n
            
            for route_id in stop_to_routes[stop]:
                if route_id not in visited:
                    visited.add(route_id)
                    for neighbour in routes[route_id]:
                        queue.append((neighbour, n+1))
        
        return -1
