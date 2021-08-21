'''
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
'''


class Solution:
    #method 1. BFS.
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        adjList = self.convertTograph(routes)
        count = 0
        queue = collections.deque(adjList[source])
        visited = set(adjList[source])
        while queue:
            count += 1
            for _ in range(len(queue)):
                curr_route = queue.popleft()
                for stop in routes[curr_route]:
                    if stop == target: return count
                    else:
                        for route_num in adjList[stop]:
                            if route_num not in visited:
                                queue.append(route_num)
                                visited.add(route_num)    
        return -1
        
        
    def convertTograph(self, routes):
        adjList = {}
        for route_num, route in enumerate(routes):
            for stop in route:
                if stop not in adjList:
                    adjList[stop] = [route_num]
                else:
                    adjList[stop].append(route_num)
        return adjList
