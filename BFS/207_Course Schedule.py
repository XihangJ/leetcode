'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

class Solution:
    #method 1. topological sorting. BFS. O(V + E), S(V)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        degree = self.findDegree(numCourses, prerequisites)
        queue = collections.deque([])
        for course in degree:
            if degree[course][0] == 0:
                queue.append(course)
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1
            for course in degree[curr][1]:
                degree[course][0] -= 1
                if degree[course][0] == 0:
                    queue.append(course)
        return count == numCourses
        
        
    def findDegree(self, numCourses, prerequisites):
        degree = {}
        for i in range(numCourses):
            degree[i] = [0, []]
        for pair in prerequisites:
            c1, c2 = pair
            degree[c1][0] += 1
            degree[c2][1].append(c1)
        return degree
