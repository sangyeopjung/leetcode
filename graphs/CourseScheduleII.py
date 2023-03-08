# https://leetcode.com/problems/course-schedule-ii/description/
# tags: topological sort, graph, bfs

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1
        
        out = []
        cantake = [course for course in range(numCourses) if not indegrees[course]]
        while cantake:
            course = cantake.pop()
            out.append(course)
            for neighbour in adj[course]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    cantake.append(neighbour)
        
        return out if len(out) == numCourses else []