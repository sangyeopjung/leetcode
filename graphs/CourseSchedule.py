# https://leetcode.com/problems/course-schedule/description/
# tags: graph, topological sort, dfs, cycle

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for n in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = [False for _ in range(numCourses)]
        in_stack = [False for _ in range(numCourses)]
        for node in range(numCourses):
            if not visited[node] and self.is_cycle(adj, node, visited, in_stack):
                return False
        
        return True
    
    def is_cycle(self, adj, node, visited, in_stack):
        if in_stack[node]:
            return True
        
        if visited[node]:
            return False
        
        in_stack[node] = True
        visited[node] = True
        for neighbour in adj[node]:
            if self.is_cycle(adj, neighbour, visited, in_stack):
                return True

        in_stack[node] = False
        return False
